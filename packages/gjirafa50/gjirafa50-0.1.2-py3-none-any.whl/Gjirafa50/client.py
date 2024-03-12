# gjirafa50_client.py

from fastapi import HTTPException
from typing import List, Optional
from .models import Product, ScrapeResult
import requests

class Gjirafa50APIClient:
    def __init__(self, base_url: str, valid_api_keys: List[str]):
        self.base_url = base_url
        self.valid_api_keys = valid_api_keys

    def authenticate_api_key(self, api_key: str):
        if api_key not in self.valid_api_keys:
            raise HTTPException(status_code=403, detail="Unauthorized access")
        else:
            print(f"User with API key '{api_key}' is authenticated")

    def search_products(self, api_key: str, pagenumber: int = 1, orderby: str = "10", q: str = "laptop",
                        advs: bool = False, hls: bool = False, is_param: bool = False,
                        startprice: Optional[int] = None, maxprice: Optional[int] = None,
                        underscore: int = 1710025383220) -> ScrapeResult:
        self.authenticate_api_key(api_key)
        params = {
            "pagenumber": pagenumber,
            "orderby": orderby,
            "q": q,
            "advs": advs,
            "hls": hls,
            "is": is_param,
            "_": underscore
        }
        if startprice is not None and maxprice is not None:
            params["price"] = f"{startprice}-{maxprice}"
        response = requests.get(f"{self.base_url}/api/search", params=params)
        response.raise_for_status()
        return ScrapeResult(**response.json())

    def get_product_details(self, api_key: str, product_url: str) -> dict:
        self.authenticate_api_key(api_key)
        response = requests.get(f"{self.base_url}/api/product/details", params={"product_url": product_url})
        response.raise_for_status()
        return response.json()
