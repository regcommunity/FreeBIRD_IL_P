from pybirdai.bird_data_model import *
from pybirdai.process_steps.pybird.orchestration import Orchestration
from pybirdai.process_steps.pybird.csv_converter import CSVConverter
from datetime import datetime
from pybirdai.annotations.decorators import lineage

class F_42_00_REF_FINREP_3_0_UnionItem:
	base = None #F_42_00_REF_FINREP_3_0_Base
	@lineage(dependencies={"base.CRRYNG_AMNT"})
	def CRRYNG_AMNT(self) -> int:
		return self.base.CRRYNG_AMNT()

class F_42_00_REF_FINREP_3_0_Base:
	def CRRYNG_AMNT() -> int:
		pass

class F_42_00_REF_FINREP_3_0_UnionTable :
	F_42_00_REF_FINREP_3_0_UnionItems = [] # F_42_00_REF_FINREP_3_0_UnionItem []
	F_42_00_REF_FINREP_3_0_Intangible_assets_other_than_Goodwill_Table = None # Intangible_assets_other_than_Goodwill
	def calc_F_42_00_REF_FINREP_3_0_UnionItems(self) -> list[F_42_00_REF_FINREP_3_0_UnionItem] :
		items = [] # F_42_00_REF_FINREP_3_0_UnionItem []
		for item in self.F_42_00_REF_FINREP_3_0_Intangible_assets_other_than_Goodwill_Table.Intangible_assets_other_than_Goodwills:
			newItem = F_42_00_REF_FINREP_3_0_UnionItem()
			newItem.base = item
			items.append(newItem)
		return items

	def init(self):
		Orchestration().init(self)
		self.F_42_00_REF_FINREP_3_0_UnionItems = []
		self.F_42_00_REF_FINREP_3_0_UnionItems.extend(self.calc_F_42_00_REF_FINREP_3_0_UnionItems())
		CSVConverter.persist_object_as_csv(self,True)
		return None


class Intangible_assets_other_than_Goodwill(F_42_00_REF_FINREP_3_0_Base):
	NN_FNNCL_ASST = None # NN_FNNCL_ASST
	@lineage(dependencies={"NN_FNNCL_ASST.CRRYNG_AMNT"})
	def CRRYNG_AMNT(self):
		return self.NN_FNNCL_ASST.CRRYNG_AMNT

class F_42_00_REF_FINREP_3_0_Intangible_assets_other_than_Goodwill_Table:
	NN_FNNCL_ASST_Table = None # NN_FNNCL_ASST
	Intangible_assets_other_than_Goodwills = []# Intangible_assets_other_than_Goodwill[]
	def calc_Intangible_assets_other_than_Goodwills(self) :
		items = [] # Intangible_assets_other_than_Goodwill[
		# Join up any refered tables that you need to join
		# loop through the main table
		# set any references you want to on the new Item so that it can refer to themin operations
		return items
	def init(self):
		Orchestration().init(self)
		self.Intangible_assets_other_than_Goodwills = []
		self.Intangible_assets_other_than_Goodwills.extend(self.calc_Intangible_assets_other_than_Goodwills())
		CSVConverter.persist_object_as_csv(self,True)
		return None

