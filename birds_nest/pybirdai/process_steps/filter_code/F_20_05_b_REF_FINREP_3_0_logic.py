from pybirdai.bird_data_model import *
from pybirdai.process_steps.pybird.orchestration import Orchestration
from pybirdai.process_steps.pybird.csv_converter import CSVConverter
from datetime import datetime
from pybirdai.annotations.decorators import lineage

class F_20_05_b_REF_FINREP_3_0_UnionItem:
	base = None #F_20_05_b_REF_FINREP_3_0_Base
	@lineage(dependencies={"base.TYP_ACCNTNG_ITM"})
	def TYP_ACCNTNG_ITM(self) -> str:
		''' return string from TYP_ACCNTNG_ITM enumeration '''
		return self.base.TYP_ACCNTNG_ITM()
	@lineage(dependencies={"base.NGTBL_SCRTY_INDCTR"})
	def NGTBL_SCRTY_INDCTR(self) -> str:
		''' return string from NGTBL_SCRTY enumeration '''
		return self.base.NGTBL_SCRTY_INDCTR()

class F_20_05_b_REF_FINREP_3_0_Base:
	def TYP_ACCNTNG_ITM() -> str:
		''' return string from TYP_ACCNTNG_ITM enumeration '''
		pass
	def NGTBL_SCRTY_INDCTR() -> str:
		''' return string from NGTBL_SCRTY enumeration '''
		pass

class F_20_05_b_REF_FINREP_3_0_UnionTable :
	F_20_05_b_REF_FINREP_3_0_UnionItems = [] # F_20_05_b_REF_FINREP_3_0_UnionItem []
	F_20_05_b_REF_FINREP_3_0_Provisions_Table = None # Provisions
	def calc_F_20_05_b_REF_FINREP_3_0_UnionItems(self) -> list[F_20_05_b_REF_FINREP_3_0_UnionItem] :
		items = [] # F_20_05_b_REF_FINREP_3_0_UnionItem []
		for item in self.F_20_05_b_REF_FINREP_3_0_Provisions_Table.Provisionss:
			newItem = F_20_05_b_REF_FINREP_3_0_UnionItem()
			newItem.base = item
			items.append(newItem)
		return items

	def init(self):
		Orchestration().init(self)
		self.F_20_05_b_REF_FINREP_3_0_UnionItems = []
		self.F_20_05_b_REF_FINREP_3_0_UnionItems.extend(self.calc_F_20_05_b_REF_FINREP_3_0_UnionItems())
		CSVConverter.persist_object_as_csv(self,True)
		return None


class Provisions(F_20_05_b_REF_FINREP_3_0_Base):
	NN_FNNCL_ASST = None # NN_FNNCL_ASST
	@lineage(dependencies={"NN_FNNCL_ASST.TYP_NN_FNNCL_ASST"})
	def TYP_ACCNTNG_ITM(self):
		return self.NN_FNNCL_ASST.TYP_NN_FNNCL_ASST

class F_20_05_b_REF_FINREP_3_0_Provisions_Table:
	NN_FNNCL_ASST_Table = None # NN_FNNCL_ASST
	Provisionss = []# Provisions[]
	def calc_Provisionss(self) :
		items = [] # Provisions[
		# Join up any refered tables that you need to join
		# loop through the main table
		# set any references you want to on the new Item so that it can refer to themin operations
		return items
	def init(self):
		Orchestration().init(self)
		self.Provisionss = []
		self.Provisionss.extend(self.calc_Provisionss())
		CSVConverter.persist_object_as_csv(self,True)
		return None

