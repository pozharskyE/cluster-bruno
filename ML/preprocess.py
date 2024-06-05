import pandas as pd
from torch.utils.data import Dataset, DataLoader
import torch

def preprocess(anime_csv, animelist_csv, users_sample_size):
    try:
        df = pd.read_csv('cached_preprocessed_df.csv')
        print('Found cached preprocessed df!')
        return df
    except Exception:
        pass

    anime = pd.read_csv('./data/2020/anime.csv')
    animelist = pd.read_csv('./data/2020/animelist.csv')

    anime.rename(columns={'MAL_ID': 'item_id'}, inplace=True)
    animelist.rename(columns={'anime_id': 'item_id'}, inplace=True)

    anime_s = (anime[anime['Genres'].str.contains('Hentai') == False])
    animelist_s = animelist[animelist['item_id'].isin(anime_s['item_id'])]

    ids = pd.Series(animelist_s['user_id'].unique())

    sample_ids = ids.sample(users_sample_size, random_state=42)

    animelist_s = animelist_s[animelist_s['user_id'].isin(sample_ids)]

    anime_s.reset_index(drop=True)
    animelist_s.reset_index(drop=True)

    df = animelist_s[['user_id', 'item_id', 'rating']]
    # df.loc[:, 'rating'] = df['rating'] / (df['rating']).max()

    df.to_csv('cached_preprocessed_df.csv', index=False)
    return df


def preprocess_and_return_loaders(anime_csv, animelist_csv, users_sample_size=10000, batch_size=128):
    df = preprocess(anime_csv, animelist_csv, users_sample_size=users_sample_size)

    class CustomDataset(Dataset):
        def __init__(self, df):
            self.X = torch.tensor(df[['user_id', 'item_id']].values, dtype=torch.int32)
            self.y = torch.tensor(df['rating'].values, dtype=torch.float32)

        def __len__(self):
            return len(self.y)

        def __getitem__(self, idx):
            return self.X[idx], self.y[idx]

    dataset = CustomDataset(df)
    
    return DataLoader(dataset, batch_size=batch_size, shuffle=True)