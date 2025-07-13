from pybirdai.bird_data_model import *
from pybirdai.process_steps.pybird.orchestration import Orchestration
from pybirdai.process_steps.pybird.csv_converter import CSVConverter
from datetime import datetime
from pybirdai.annotations.decorators import lineage

class F_21_00_REF_FINREP_3_0_UnionItem:
	base = None #F_21_00_REF_FINREP_3_0_Base
	@lineage(dependencies={"base.CRRYNG_AMNT"})
	def CRRYNG_AMNT(self) -> int:
		return self.base.CRRYNG_AMNT()
	@lineage(dependencies={"base.ACCNTNG_CLSSFCTN"})
	def ACCNTNG_CLSSFCTN(self) -> str:
		''' return string from ACCNTNG_CLSSFCTN enumeration '''
		return self.base.ACCNTNG_CLSSFCTN()
	@lineage(dependencies={"base.TYP_ACCNTNG_ITM"})
	def TYP_ACCNTNG_ITM(self) -> str:
		''' return string from TYP_ACCNTNG_ITM enumeration '''
		return self.base.TYP_ACCNTNG_ITM()
	@lineage(dependencies={"base.HLD_SL_INDCTR"})
	def HLD_SL_INDCTR(self) -> str:
		''' return string from HLD_SL_INDCTR enumeration '''
		return self.base.HLD_SL_INDCTR()
	@lineage(dependencies={"base.MSRMNT_MTHD"})
	def MSRMNT_MTHD(self) -> str:
		''' return string from MSRMNT_MTHD enumeration '''
		return self.base.MSRMNT_MTHD()
	@lineage(dependencies={"base.SBJCT_IMPRMNT_INDCTR"})
	def SBJCT_IMPRMNT_INDCTR(self) -> str:
		''' return string from SBJCT_IMPRMNT_INDCTR enumeration '''
		return self.base.SBJCT_IMPRMNT_INDCTR()
	@lineage(dependencies={"base.NGTBL_SCRTY_INDCTR"})
	def NGTBL_SCRTY_INDCTR(self) -> str:
		''' return string from NGTBL_SCRTY enumeration '''
		return self.base.NGTBL_SCRTY_INDCTR()
	@lineage(dependencies={"base.SBJCT_OPRTNG_LS_INDCTR"})
	def SBJCT_OPRTNG_LS_INDCTR(self) -> str:
		''' return string from SBJCT_OPRTNG_LS_INDCTR enumeration '''
		return self.base.SBJCT_OPRTNG_LS_INDCTR()

class F_21_00_REF_FINREP_3_0_Base:
	def CRRYNG_AMNT() -> int:
		pass
	def ACCNTNG_CLSSFCTN() -> str:
		''' return string from ACCNTNG_CLSSFCTN enumeration '''
		pass
	def TYP_ACCNTNG_ITM() -> str:
		''' return string from TYP_ACCNTNG_ITM enumeration '''
		pass
	def HLD_SL_INDCTR() -> str:
		''' return string from HLD_SL_INDCTR enumeration '''
		pass
	def MSRMNT_MTHD() -> str:
		''' return string from MSRMNT_MTHD enumeration '''
		pass
	def SBJCT_IMPRMNT_INDCTR() -> str:
		''' return string from SBJCT_IMPRMNT_INDCTR enumeration '''
		pass
	def NGTBL_SCRTY_INDCTR() -> str:
		''' return string from NGTBL_SCRTY enumeration '''
		pass
	def SBJCT_OPRTNG_LS_INDCTR() -> str:
		''' return string from SBJCT_OPRTNG_LS_INDCTR enumeration '''
		pass

class F_21_00_REF_FINREP_3_0_UnionTable :
	F_21_00_REF_FINREP_3_0_UnionItems = [] # F_21_00_REF_FINREP_3_0_UnionItem []
	F_21_00_REF_FINREP_3_0_Intangible_assets_other_than_Goodwill_Table = None # Intangible_assets_other_than_Goodwill
	def calc_F_21_00_REF_FINREP_3_0_UnionItems(self) -> list[F_21_00_REF_FINREP_3_0_UnionItem] :
		items = [] # F_21_00_REF_FINREP_3_0_UnionItem []
		for item in self.F_21_00_REF_FINREP_3_0_Intangible_assets_other_than_Goodwill_Table.Intangible_assets_other_than_Goodwills:
			newItem = F_21_00_REF_FINREP_3_0_UnionItem()
			newItem.base = item
			items.append(newItem)
		return items

	def init(self):
		Orchestration().init(self)
		self.F_21_00_REF_FINREP_3_0_UnionItems = []
		self.F_21_00_REF_FINREP_3_0_UnionItems.extend(self.calc_F_21_00_REF_FINREP_3_0_UnionItems())
		CSVConverter.persist_object_as_csv(self,True)
		return None


class Intangible_assets_other_than_Goodwill(F_21_00_REF_FINREP_3_0_Base):
	NN_FNNCL_ASST = None # NN_FNNCL_ASST
	@lineage(dependencies={"NN_FNNCL_ASST.CRRYNG_AMNT"})
	def CRRYNG_AMNT(self):
		return self.NN_FNNCL_ASST.CRRYNG_AMNT
	@lineage(dependencies={"NN_FNNCL_ASST.HLD_SL_INDCTR"})
	def HLD_SL_INDCTR(self):
		return self.NN_FNNCL_ASST.HLD_SL_INDCTR
	@lineage(dependencies={"NN_FNNCL_ASST.MSRMNT_MTHD"})
	def MSRMNT_MTHD(self):
		return self.NN_FNNCL_ASST.MSRMNT_MTHD
	@lineage(dependencies={"NN_FNNCL_ASST.SBJCT_OPRTNG_LS_INDCTR"})
	def SBJCT_OPRTNG_LS_INDCTR(self):
		return self.NN_FNNCL_ASST.SBJCT_OPRTNG_LS_INDCTR
	@lineage(dependencies={"NN_FNNCL_ASST.TYP_NN_FNNCL_ASST"})
	def TYP_ACCNTNG_ITM(self):
		return self.NN_FNNCL_ASST.TYP_NN_FNNCL_ASST

class F_21_00_REF_FINREP_3_0_Intangible_assets_other_than_Goodwill_Table:
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

