import asyncio
from typing import Optional

from komoutils.core import KomoBase
from pydantic import BaseModel

from aporacle.intervaled_data_symbol.client.orchestrator import Orchestrator


class AssetPriceData(BaseModel):
    chain: str
    epoch: int
    asset: str
    price: float


class IntervaledTradingSymbolExecutor(KomoBase):

    def __init__(self,
                 symbol: str,
                 input_queue: asyncio.Queue,
                 output_queue: asyncio.Queue,
                 output_record_evaluation_ticks: int = 18
                 ):
        super().__init__()
        self.symbol: str = symbol
        self.asset: str = self.symbol.split("_")[-2]
        self.input_queue: asyncio.Queue = input_queue
        self.output_queue: asyncio.Queue = output_queue
        self.output_record_evaluation_ticks = output_record_evaluation_ticks
        self.orchestrator: Optional[Orchestrator] = None

    @property
    def name(self):
        return "intervaled_trading_symbol_executor"

    def start(self):
        self.orchestrator = Orchestrator(
            symbol=self.symbol,
            input_queue=self.input_queue,
            output_queue=self.output_queue,
            output_record_evaluation_ticks=self.output_record_evaluation_ticks,
        )
        self.orchestrator.start()

    def stop(self):
        pass

    def set_tso_data(self, asset_price_data: AssetPriceData):
        self.orchestrator.tso_price_set(chain=asset_price_data.chain,
                                        tso=asset_price_data.asset,
                                        price=asset_price_data.price)

    def process_chain_epoch(self, chain: str, epoch: int):
        return self.orchestrator.generate_chain_epoch_record(chain=chain, epoch=epoch)
