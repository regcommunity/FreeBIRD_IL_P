from pybirdai.bird_data_model import *
from pybirdai.process_steps.pybird.orchestration import Orchestration
from pybirdai.process_steps.pybird.csv_converter import CSVConverter
from datetime import datetime
from pybirdai.annotations.decorators import lineage

class F_01_01_REF_FINREP_3_0_UnionItem:
	base = None #F_01_01_REF_FINREP_3_0_Base
	@lineage(dependencies={"base.CRRYNG_AMNT"})
	def CRRYNG_AMNT(self) -> int:
		return self.base.CRRYNG_AMNT()
	@lineage(dependencies={"base.ACCNTNG_CLSSFCTN"})
	def ACCNTNG_CLSSFCTN(self) -> str:
		''' return string from ACCNTNG_CLSSFCTN enumeration '''
		return self.base.ACCNTNG_CLSSFCTN()
	@lineage(dependencies={"base.TYP_INSTRMNT"})
	def TYP_INSTRMNT(self) -> str:
		''' return string from TYP_INSTRMNT enumeration '''
		return self.base.TYP_INSTRMNT()
	@lineage(dependencies={"base.HLD_SL_INDCTR"})
	def HLD_SL_INDCTR(self) -> str:
		''' return string from HLD_SL_INDCTR enumeration '''
		return self.base.HLD_SL_INDCTR()
	@lineage(dependencies={"base.RPYMNT_RGHTS"})
	def RPYMNT_RGHTS(self) -> str:
		''' return string from RPYMNT_RGHTS enumeration '''
		return self.base.RPYMNT_RGHTS()
	@lineage(dependencies={"base.INSTTTNL_SCTR"})
	def INSTTTNL_SCTR(self) -> str:
		''' return string from INSTTTNL_SCTR enumeration '''
		return self.base.INSTTTNL_SCTR()
	@lineage(dependencies={"base.PRTY_RL_TYP"})
	def PRTY_RL_TYP(self) -> str:
		''' return string from ENTTY_RL_TYP enumeration '''
		return self.base.PRTY_RL_TYP()
	@lineage(dependencies={"base.MN_DBTR_INDCTR"})
	def MN_DBTR_INDCTR(self) -> str:
		''' return string from MN_DBTR_INDCTR enumeration '''
		return self.base.MN_DBTR_INDCTR()
	@lineage(dependencies={"base.NGTBL_SCRTY_INDCTR"})
	def NGTBL_SCRTY_INDCTR(self) -> str:
		''' return string from NGTBL_SCRTY enumeration '''
		return self.base.NGTBL_SCRTY_INDCTR()
	@lineage(dependencies={"base.SCRTY_EXCHNG_TRDBL_DRVTV_TYP"})
	def SCRTY_EXCHNG_TRDBL_DRVTV_TYP(self) -> str:
		''' return string from SCRTY_EXCHNG_TRDBL_DRVTV_TYP enumeration '''
		return self.base.SCRTY_EXCHNG_TRDBL_DRVTV_TYP()
	@lineage(dependencies={"base.TYP_ACCNTNG_ITM"})
	def TYP_ACCNTNG_ITM(self) -> str:
		''' return string from TYP_ACCNTNG_ITM enumeration '''
		return self.base.TYP_ACCNTNG_ITM()
	@lineage(dependencies={"base.TYP_HDG"})
	def TYP_HDG(self) -> str:
		''' return string from TYP_HDG enumeration '''
		return self.base.TYP_HDG()

class F_01_01_REF_FINREP_3_0_Base:
	def CRRYNG_AMNT() -> int:
		pass
	def ACCNTNG_CLSSFCTN() -> str:
		''' return string from ACCNTNG_CLSSFCTN enumeration '''
		pass
	def TYP_INSTRMNT() -> str:
		''' return string from TYP_INSTRMNT enumeration '''
		pass
	def HLD_SL_INDCTR() -> str:
		''' return string from HLD_SL_INDCTR enumeration '''
		pass
	def RPYMNT_RGHTS() -> str:
		''' return string from RPYMNT_RGHTS enumeration '''
		pass
	def INSTTTNL_SCTR() -> str:
		''' return string from INSTTTNL_SCTR enumeration '''
		pass
	def PRTY_RL_TYP() -> str:
		''' return string from ENTTY_RL_TYP enumeration '''
		pass
	def MN_DBTR_INDCTR() -> str:
		''' return string from MN_DBTR_INDCTR enumeration '''
		pass
	def NGTBL_SCRTY_INDCTR() -> str:
		''' return string from NGTBL_SCRTY enumeration '''
		pass
	def SCRTY_EXCHNG_TRDBL_DRVTV_TYP() -> str:
		''' return string from SCRTY_EXCHNG_TRDBL_DRVTV_TYP enumeration '''
		pass
	def TYP_ACCNTNG_ITM() -> str:
		''' return string from TYP_ACCNTNG_ITM enumeration '''
		pass
	def TYP_HDG() -> str:
		''' return string from TYP_HDG enumeration '''
		pass

class F_01_01_REF_FINREP_3_0_UnionTable :
	F_01_01_REF_FINREP_3_0_UnionItems = [] # F_01_01_REF_FINREP_3_0_UnionItem []
	F_01_01_REF_FINREP_3_0_Equity_instruments_Table = None # Equity_instruments
	F_01_01_REF_FINREP_3_0_Debt_securities_Table = None # Debt_securities
	F_01_01_REF_FINREP_3_0_Derivatives_Table = None # Derivatives
	F_01_01_REF_FINREP_3_0_Intangible_assets_Goodwill_Table = None # Intangible_assets_Goodwill
	F_01_01_REF_FINREP_3_0_Non_current_assets_and_disposal_groups_classified_as_held_for_sale_Table = None # Non_current_assets_and_disposal_groups_classified_as_held_for_sale
	F_01_01_REF_FINREP_3_0_Intangible_assets_Table = None # Intangible_assets
	F_01_01_REF_FINREP_3_0_Deferred_tax_assets_Table = None # Deferred_tax_assets
	F_01_01_REF_FINREP_3_0_Tangible_assets_Table = None # Tangible_assets
	F_01_01_REF_FINREP_3_0_Intangible_assets_other_than_Goodwill_Table = None # Intangible_assets_other_than_Goodwill
	F_01_01_REF_FINREP_3_0_Tax_assets_Table = None # Tax_assets
	F_01_01_REF_FINREP_3_0_Tangible_assets_Investment_property_Table = None # Tangible_assets_Investment_property
	F_01_01_REF_FINREP_3_0_Current_tax_assets_Table = None # Current_tax_assets
	def calc_F_01_01_REF_FINREP_3_0_UnionItems(self) -> list[F_01_01_REF_FINREP_3_0_UnionItem] :
		items = [] # F_01_01_REF_FINREP_3_0_UnionItem []
		for item in self.F_01_01_REF_FINREP_3_0_Equity_instruments_Table.Equity_instrumentss:
			newItem = F_01_01_REF_FINREP_3_0_UnionItem()
			newItem.base = item
			items.append(newItem)
		for item in self.F_01_01_REF_FINREP_3_0_Debt_securities_Table.Debt_securitiess:
			newItem = F_01_01_REF_FINREP_3_0_UnionItem()
			newItem.base = item
			items.append(newItem)
		for item in self.F_01_01_REF_FINREP_3_0_Derivatives_Table.Derivativess:
			newItem = F_01_01_REF_FINREP_3_0_UnionItem()
			newItem.base = item
			items.append(newItem)
		for item in self.F_01_01_REF_FINREP_3_0_Intangible_assets_Goodwill_Table.Intangible_assets_Goodwills:
			newItem = F_01_01_REF_FINREP_3_0_UnionItem()
			newItem.base = item
			items.append(newItem)
		for item in self.F_01_01_REF_FINREP_3_0_Non_current_assets_and_disposal_groups_classified_as_held_for_sale_Table.Non_current_assets_and_disposal_groups_classified_as_held_for_sales:
			newItem = F_01_01_REF_FINREP_3_0_UnionItem()
			newItem.base = item
			items.append(newItem)
		for item in self.F_01_01_REF_FINREP_3_0_Intangible_assets_Table.Intangible_assetss:
			newItem = F_01_01_REF_FINREP_3_0_UnionItem()
			newItem.base = item
			items.append(newItem)
		for item in self.F_01_01_REF_FINREP_3_0_Deferred_tax_assets_Table.Deferred_tax_assetss:
			newItem = F_01_01_REF_FINREP_3_0_UnionItem()
			newItem.base = item
			items.append(newItem)
		for item in self.F_01_01_REF_FINREP_3_0_Tangible_assets_Table.Tangible_assetss:
			newItem = F_01_01_REF_FINREP_3_0_UnionItem()
			newItem.base = item
			items.append(newItem)
		for item in self.F_01_01_REF_FINREP_3_0_Intangible_assets_other_than_Goodwill_Table.Intangible_assets_other_than_Goodwills:
			newItem = F_01_01_REF_FINREP_3_0_UnionItem()
			newItem.base = item
			items.append(newItem)
		for item in self.F_01_01_REF_FINREP_3_0_Tax_assets_Table.Tax_assetss:
			newItem = F_01_01_REF_FINREP_3_0_UnionItem()
			newItem.base = item
			items.append(newItem)
		for item in self.F_01_01_REF_FINREP_3_0_Tangible_assets_Investment_property_Table.Tangible_assets_Investment_propertys:
			newItem = F_01_01_REF_FINREP_3_0_UnionItem()
			newItem.base = item
			items.append(newItem)
		for item in self.F_01_01_REF_FINREP_3_0_Current_tax_assets_Table.Current_tax_assetss:
			newItem = F_01_01_REF_FINREP_3_0_UnionItem()
			newItem.base = item
			items.append(newItem)
		return items

	def init(self):
		Orchestration().init(self)
		self.F_01_01_REF_FINREP_3_0_UnionItems = []
		self.F_01_01_REF_FINREP_3_0_UnionItems.extend(self.calc_F_01_01_REF_FINREP_3_0_UnionItems())
		CSVConverter.persist_object_as_csv(self,True)
		return None


class Equity_instruments(F_01_01_REF_FINREP_3_0_Base):
	EQTY_FND_SCRTY = None # EQTY_FND_SCRTY
	@lineage(dependencies={"EQTY_FND_SCRTY.EQTY_FND_SCRTY_TYP"})
	def SCRTY_EXCHNG_TRDBL_DRVTV_TYP(self):
		return self.EQTY_FND_SCRTY.EQTY_FND_SCRTY_TYP
	LNG_EQUTY_FND_SCRTY_PSTN_PRDNTL_PRFL_ASSGNMNT_ACCNTNG_CLSSFCTN_ASST_ASSGNMNT_IFRS = None # LNG_EQUTY_FND_SCRTY_PSTN_PRDNTL_PRFL_ASSGNMNT_ACCNTNG_CLSSFCTN_ASST_ASSGNMNT_IFRS
	@lineage(dependencies={"LNG_EQUTY_FND_SCRTY_PSTN_PRDNTL_PRFL_ASSGNMNT_ACCNTNG_CLSSFCTN_ASST_ASSGNMNT_IFRS.HLD_SL_INDCTR"})
	def HLD_SL_INDCTR(self):
		return self.LNG_EQUTY_FND_SCRTY_PSTN_PRDNTL_PRFL_ASSGNMNT_ACCNTNG_CLSSFCTN_ASST_ASSGNMNT_IFRS.HLD_SL_INDCTR
	LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FR_FNNCL_ASSTS_ASSGNMNT_DRVD_DT = None # LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FR_FNNCL_ASSTS_ASSGNMNT_DRVD_DT
	@lineage(dependencies={"LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FR_FNNCL_ASSTS_ASSGNMNT_DRVD_DT.ACCNTNG_CLSSFCTN"})
	def ACCNTNG_CLSSFCTN(self):
		return self.LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FR_FNNCL_ASSTS_ASSGNMNT_DRVD_DT.ACCNTNG_CLSSFCTN
	@lineage(dependencies={"LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FR_FNNCL_ASSTS_ASSGNMNT_DRVD_DT.INVSTR_PRTY_RL_TYP"})
	def PRTY_RL_TYP(self):
		return self.LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FR_FNNCL_ASSTS_ASSGNMNT_DRVD_DT.INVSTR_PRTY_RL_TYP
	LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASSTS_ASSGNMNT = None # LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASSTS_ASSGNMNT
	@lineage(dependencies={"LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASSTS_ASSGNMNT.CRRYNG_AMNT"})
	def CRRYNG_AMNT(self):
		return self.LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASSTS_ASSGNMNT.CRRYNG_AMNT
	@lineage(dependencies={"LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASSTS_ASSGNMNT.ACCNTNG_CLSSFCTN"})
	def ACCNTNG_CLSSFCTN(self):
		return self.LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASSTS_ASSGNMNT.ACCNTNG_CLSSFCTN
	@lineage(dependencies={"LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASSTS_ASSGNMNT.INVSTR_PRTY_RL_TYP"})
	def PRTY_RL_TYP(self):
		return self.LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASSTS_ASSGNMNT.INVSTR_PRTY_RL_TYP
	LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT = None # LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT
	@lineage(dependencies={"LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT.INVSTR_PRTY_RL_TYP"})
	def PRTY_RL_TYP(self):
		return self.LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT.INVSTR_PRTY_RL_TYP
	SCRTY_PSTN = None # SCRTY_PSTN
	@lineage(dependencies={"SCRTY_PSTN.INVSTR_PRTY_RL_TYP"})
	def PRTY_RL_TYP(self):
		return self.SCRTY_PSTN.INVSTR_PRTY_RL_TYP
	LNG_SCRTY_PSTN_HDG = None # LNG_SCRTY_PSTN_HDG
	@lineage(dependencies={"LNG_SCRTY_PSTN_HDG.INVSTR_RL_TYP"})
	def PRTY_RL_TYP(self):
		return self.LNG_SCRTY_PSTN_HDG.INVSTR_RL_TYP
	@lineage(dependencies={"LNG_SCRTY_PSTN_HDG.TYP_HDG"})
	def TYP_HDG(self):
		return self.LNG_SCRTY_PSTN_HDG.TYP_HDG
	LNG_SCRTY_PSTN_DRVD_DT = None # LNG_SCRTY_PSTN_DRVD_DT
	@lineage(dependencies={"LNG_SCRTY_PSTN_DRVD_DT.INVSTR_PRTY_RL_TYP"})
	def PRTY_RL_TYP(self):
		return self.LNG_SCRTY_PSTN_DRVD_DT.INVSTR_PRTY_RL_TYP
	SCRTY = None # SCRTY
	@lineage(dependencies={"SCRTY.SCRTY_TYP_BY_IDNTFR"})
	def SCRTY_EXCHNG_TRDBL_DRVTV_TYP(self):
		return self.SCRTY.SCRTY_TYP_BY_IDNTFR
	@lineage(dependencies={"SCRTY.SCRTY_TYP_BY_PRDCT"})
	def SCRTY_EXCHNG_TRDBL_DRVTV_TYP(self):
		return self.SCRTY.SCRTY_TYP_BY_PRDCT
	SCRTY_ISSR_ASSGNMNT = None # SCRTY_ISSR_ASSGNMNT
	@lineage(dependencies={"SCRTY_ISSR_ASSGNMNT.PRTY_RL_TYP"})
	def PRTY_RL_TYP(self):
		return self.SCRTY_ISSR_ASSGNMNT.PRTY_RL_TYP
	PRTY_RL = None # PRTY_RL
	@lineage(dependencies={"PRTY_RL.PRTY_RL_TYP"})
	def PRTY_RL_TYP(self):
		return self.PRTY_RL.PRTY_RL_TYP
	ENTTY_RL = None # ENTTY_RL
	@lineage(dependencies={"ENTTY_RL.ENTTY_RL_TYP"})
	def PRTY_RL_TYP(self):
		return self.ENTTY_RL.ENTTY_RL_TYP
	ENTTY_TRNSCTN_RL = None # ENTTY_TRNSCTN_RL
	@lineage(dependencies={"ENTTY_TRNSCTN_RL.ENTTY_TRNSCTN_RL_TYP"})
	def PRTY_RL_TYP(self):
		return self.ENTTY_TRNSCTN_RL.ENTTY_TRNSCTN_RL_TYP
	PRTY = None # PRTY
	@lineage(dependencies={"PRTY.INSTTTNL_SCTR"})
	def INSTTTNL_SCTR(self):
		return self.PRTY.INSTTTNL_SCTR
	PRTY_DRVD_DT = None # PRTY_DRVD_DT
	@lineage(dependencies={"PRTY_DRVD_DT.INSTTNL_SCTR_EBA_ITS"})
	def INSTTTNL_SCTR(self):
		return self.PRTY_DRVD_DT.INSTTNL_SCTR_EBA_ITS
	@lineage(dependencies={"PRTY_DRVD_DT.INSTTNL_SCTR_SHS"})
	def INSTTTNL_SCTR(self):
		return self.PRTY_DRVD_DT.INSTTNL_SCTR_SHS
	SCRTY_EXCHNG_TRDBL_DRVTV = None # SCRTY_EXCHNG_TRDBL_DRVTV
	@lineage(dependencies={"SCRTY_EXCHNG_TRDBL_DRVTV.SCRTY_EXCHNG_TRDBL_DRVTV_TYP"})
	def SCRTY_EXCHNG_TRDBL_DRVTV_TYP(self):
		return self.SCRTY_EXCHNG_TRDBL_DRVTV.SCRTY_EXCHNG_TRDBL_DRVTV_TYP

class Debt_securities(F_01_01_REF_FINREP_3_0_Base):
	pass
	LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASSTS_ASSGNMNT = None # LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASSTS_ASSGNMNT
	@lineage(dependencies={"LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASSTS_ASSGNMNT.CRRYNG_AMNT"})
	def CRRYNG_AMNT(self):
		return self.LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASSTS_ASSGNMNT.CRRYNG_AMNT
	@lineage(dependencies={"LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASSTS_ASSGNMNT.ACCNTNG_CLSSFCTN"})
	def ACCNTNG_CLSSFCTN(self):
		return self.LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASSTS_ASSGNMNT.ACCNTNG_CLSSFCTN
	pass
	PRTY = None # PRTY
	@lineage(dependencies={"PRTY.INSTTTNL_SCTR"})
	def INSTTTNL_SCTR(self):
		return self.PRTY.INSTTTNL_SCTR
	ISIN_SCRTY = None # ISIN_SCRTY
	@lineage(dependencies={"ISIN_SCRTY.NGTBL_SCRTY_INDCTR"})
	def NGTBL_SCRTY_INDCTR(self):
		return self.ISIN_SCRTY.NGTBL_SCRTY_INDCTR
	pass
	pass
	LNG_SCRTY_PSTN_HDG = None # LNG_SCRTY_PSTN_HDG
	@lineage(dependencies={"LNG_SCRTY_PSTN_HDG.TYP_HDG"})
	def TYP_HDG(self):
		return self.LNG_SCRTY_PSTN_HDG.TYP_HDG
	pass
	pass
	SCRTY_ISSR_ASSGNMNT = None # SCRTY_ISSR_ASSGNMNT
	@lineage(dependencies={"SCRTY_ISSR_ASSGNMNT.PRTY_RL_TYP"})
	def PRTY_RL_TYP(self):
		return self.SCRTY_ISSR_ASSGNMNT.PRTY_RL_TYP
	pass
	pass
	pass
	pass
	pass
	DBT_SCRTY = None # DBT_SCRTY
	@lineage(dependencies={"DBT_SCRTY.DBT_SCRTY_TYP"})
	def SCRTY_EXCHNG_TRDBL_DRVTV_TYP(self):
		return self.DBT_SCRTY.DBT_SCRTY_TYP
	LNG_DBT_SCRTY_PSTN_PRDNTL_PRFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASSTS_ASSGNMNT_IFRS = None # LNG_DBT_SCRTY_PSTN_PRDNTL_PRFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASSTS_ASSGNMNT_IFRS
	@lineage(dependencies={"LNG_DBT_SCRTY_PSTN_PRDNTL_PRFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASSTS_ASSGNMNT_IFRS.HLD_SL_INDCTR"})
	def HLD_SL_INDCTR(self):
		return self.LNG_DBT_SCRTY_PSTN_PRDNTL_PRFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASSTS_ASSGNMNT_IFRS.HLD_SL_INDCTR

class Derivatives(F_01_01_REF_FINREP_3_0_Base):
	EXCHNG_TRDBL_DRVTV_PSTN = None # EXCHNG_TRDBL_DRVTV_PSTN
	@lineage(dependencies={"EXCHNG_TRDBL_DRVTV_PSTN.HLD_SL_INDCTR"})
	def HLD_SL_INDCTR(self):
		return self.EXCHNG_TRDBL_DRVTV_PSTN.HLD_SL_INDCTR
	@lineage(dependencies={"EXCHNG_TRDBL_DRVTV_PSTN.BYR_PRTY_RL_TYP"})
	def PRTY_RL_TYP(self):
		return self.EXCHNG_TRDBL_DRVTV_PSTN.BYR_PRTY_RL_TYP
	@lineage(dependencies={"EXCHNG_TRDBL_DRVTV_PSTN.SLLR_PRTY_RL_TYP"})
	def PRTY_RL_TYP(self):
		return self.EXCHNG_TRDBL_DRVTV_PSTN.SLLR_PRTY_RL_TYP
	PRTY = None # PRTY
	@lineage(dependencies={"PRTY.INSTTTNL_SCTR"})
	def INSTTTNL_SCTR(self):
		return self.PRTY.INSTTTNL_SCTR
	PRTY_DRVD_DT = None # PRTY_DRVD_DT
	@lineage(dependencies={"PRTY_DRVD_DT.INSTTNL_SCTR_EBA_ITS"})
	def INSTTTNL_SCTR(self):
		return self.PRTY_DRVD_DT.INSTTNL_SCTR_EBA_ITS
	@lineage(dependencies={"PRTY_DRVD_DT.INSTTNL_SCTR_SHS"})
	def INSTTTNL_SCTR(self):
		return self.PRTY_DRVD_DT.INSTTNL_SCTR_SHS
	PRTY_RL = None # PRTY_RL
	@lineage(dependencies={"PRTY_RL.PRTY_RL_TYP"})
	def PRTY_RL_TYP(self):
		return self.PRTY_RL.PRTY_RL_TYP
	ENTTY_RL = None # ENTTY_RL
	@lineage(dependencies={"ENTTY_RL.ENTTY_RL_TYP"})
	def PRTY_RL_TYP(self):
		return self.ENTTY_RL.ENTTY_RL_TYP
	ENTTY_TRNSCTN_RL = None # ENTTY_TRNSCTN_RL
	@lineage(dependencies={"ENTTY_TRNSCTN_RL.ENTTY_TRNSCTN_RL_TYP"})
	def PRTY_RL_TYP(self):
		return self.ENTTY_TRNSCTN_RL.ENTTY_TRNSCTN_RL_TYP
	pass
	SCRTY_EXCHNG_TRDBL_DRVTV = None # SCRTY_EXCHNG_TRDBL_DRVTV
	@lineage(dependencies={"SCRTY_EXCHNG_TRDBL_DRVTV.SCRTY_EXCHNG_TRDBL_DRVTV_TYP"})
	def SCRTY_EXCHNG_TRDBL_DRVTV_TYP(self):
		return self.SCRTY_EXCHNG_TRDBL_DRVTV.SCRTY_EXCHNG_TRDBL_DRVTV_TYP
	SCRTY_ISSR_ASSGNMNT = None # SCRTY_ISSR_ASSGNMNT
	@lineage(dependencies={"SCRTY_ISSR_ASSGNMNT.PRTY_RL_TYP"})
	def PRTY_RL_TYP(self):
		return self.SCRTY_ISSR_ASSGNMNT.PRTY_RL_TYP
	OTC_DRVTV_INSTRMNT = None # OTC_DRVTV_INSTRMNT
	@lineage(dependencies={"OTC_DRVTV_INSTRMNT.OTC_DRVTV_INSTRMNT_TYP"})
	def TYP_INSTRMNT(self):
		return self.OTC_DRVTV_INSTRMNT.OTC_DRVTV_INSTRMNT_TYP
	INSTRMNT = None # INSTRMNT
	@lineage(dependencies={"INSTRMNT.INSTRMNT_TYP_ORGN"})
	def TYP_INSTRMNT(self):
		return self.INSTRMNT.INSTRMNT_TYP_ORGN
	@lineage(dependencies={"INSTRMNT.INSTRMNT_TYP_PRDCT"})
	def TYP_INSTRMNT(self):
		return self.INSTRMNT.INSTRMNT_TYP_PRDCT
	INSTRMNT_SRVCR_ASSGNMNT = None # INSTRMNT_SRVCR_ASSGNMNT
	@lineage(dependencies={"INSTRMNT_SRVCR_ASSGNMNT.SRVCR_PRTY_RL_TYP"})
	def PRTY_RL_TYP(self):
		return self.INSTRMNT_SRVCR_ASSGNMNT.SRVCR_PRTY_RL_TYP
	OTC_DRVTV_BUYR_ASSGNMNT = None # OTC_DRVTV_BUYR_ASSGNMNT
	@lineage(dependencies={"OTC_DRVTV_BUYR_ASSGNMNT.BYR_PRTY_RL_TYP"})
	def PRTY_RL_TYP(self):
		return self.OTC_DRVTV_BUYR_ASSGNMNT.BYR_PRTY_RL_TYP
	OTC_DRVTV_SLLR_ASSGNMNT = None # OTC_DRVTV_SLLR_ASSGNMNT
	@lineage(dependencies={"OTC_DRVTV_SLLR_ASSGNMNT.SLLR_PRTY_RL_TYP"})
	def PRTY_RL_TYP(self):
		return self.OTC_DRVTV_SLLR_ASSGNMNT.SLLR_PRTY_RL_TYP

class Intangible_assets_Goodwill(F_01_01_REF_FINREP_3_0_Base):
	INVSTMNT_PRPRTY = None # INVSTMNT_PRPRTY
	@lineage(dependencies={"INVSTMNT_PRPRTY.HLD_SL_INDCTR"})
	def HLD_SL_INDCTR(self):
		return self.INVSTMNT_PRPRTY.HLD_SL_INDCTR
	NN_FNNCL_ASST = None # NN_FNNCL_ASST
	@lineage(dependencies={"NN_FNNCL_ASST.NN_FNNCL_ASST_TYP"})
	def TYP_ACCNTNG_ITM(self):
		return self.NN_FNNCL_ASST.NN_FNNCL_ASST_TYP
	NN_FNNCL_ASST_NN_FNNCL_LBLTY = None # NN_FNNCL_ASST_NN_FNNCL_LBLTY
	@lineage(dependencies={"NN_FNNCL_ASST_NN_FNNCL_LBLTY.CRRYNG_AMNT"})
	def CRRYNG_AMNT(self):
		return self.NN_FNNCL_ASST_NN_FNNCL_LBLTY.CRRYNG_AMNT
	@lineage(dependencies={"NN_FNNCL_ASST_NN_FNNCL_LBLTY.NN_FNNCL_ASST_NN_FNNCL_LBLTY_TYP"})
	def TYP_ACCNTNG_ITM(self):
		return self.NN_FNNCL_ASST_NN_FNNCL_LBLTY.NN_FNNCL_ASST_NN_FNNCL_LBLTY_TYP

class Non_current_assets_and_disposal_groups_classified_as_held_for_sale(F_01_01_REF_FINREP_3_0_Base):
	INVSTMNT_PRPRTY = None # INVSTMNT_PRPRTY
	@lineage(dependencies={"INVSTMNT_PRPRTY.HLD_SL_INDCTR"})
	def HLD_SL_INDCTR(self):
		return self.INVSTMNT_PRPRTY.HLD_SL_INDCTR
	NN_FNNCL_ASST = None # NN_FNNCL_ASST
	@lineage(dependencies={"NN_FNNCL_ASST.NN_FNNCL_ASST_TYP"})
	def TYP_ACCNTNG_ITM(self):
		return self.NN_FNNCL_ASST.NN_FNNCL_ASST_TYP
	NN_FNNCL_ASST_NN_FNNCL_LBLTY = None # NN_FNNCL_ASST_NN_FNNCL_LBLTY
	@lineage(dependencies={"NN_FNNCL_ASST_NN_FNNCL_LBLTY.CRRYNG_AMNT"})
	def CRRYNG_AMNT(self):
		return self.NN_FNNCL_ASST_NN_FNNCL_LBLTY.CRRYNG_AMNT
	@lineage(dependencies={"NN_FNNCL_ASST_NN_FNNCL_LBLTY.NN_FNNCL_ASST_NN_FNNCL_LBLTY_TYP"})
	def TYP_ACCNTNG_ITM(self):
		return self.NN_FNNCL_ASST_NN_FNNCL_LBLTY.NN_FNNCL_ASST_NN_FNNCL_LBLTY_TYP

class Intangible_assets(F_01_01_REF_FINREP_3_0_Base):
	INVSTMNT_PRPRTY = None # INVSTMNT_PRPRTY
	@lineage(dependencies={"INVSTMNT_PRPRTY.HLD_SL_INDCTR"})
	def HLD_SL_INDCTR(self):
		return self.INVSTMNT_PRPRTY.HLD_SL_INDCTR
	NN_FNNCL_ASST = None # NN_FNNCL_ASST
	@lineage(dependencies={"NN_FNNCL_ASST.NN_FNNCL_ASST_TYP"})
	def TYP_ACCNTNG_ITM(self):
		return self.NN_FNNCL_ASST.NN_FNNCL_ASST_TYP
	NN_FNNCL_ASST_NN_FNNCL_LBLTY = None # NN_FNNCL_ASST_NN_FNNCL_LBLTY
	@lineage(dependencies={"NN_FNNCL_ASST_NN_FNNCL_LBLTY.CRRYNG_AMNT"})
	def CRRYNG_AMNT(self):
		return self.NN_FNNCL_ASST_NN_FNNCL_LBLTY.CRRYNG_AMNT
	@lineage(dependencies={"NN_FNNCL_ASST_NN_FNNCL_LBLTY.NN_FNNCL_ASST_NN_FNNCL_LBLTY_TYP"})
	def TYP_ACCNTNG_ITM(self):
		return self.NN_FNNCL_ASST_NN_FNNCL_LBLTY.NN_FNNCL_ASST_NN_FNNCL_LBLTY_TYP

class Deferred_tax_assets(F_01_01_REF_FINREP_3_0_Base):
	TS_ASST = None # TS_ASST
	@lineage(dependencies={"TS_ASST.HLD_SL_INDCTR"})
	def HLD_SL_INDCTR(self):
		return self.TS_ASST.HLD_SL_INDCTR
	@lineage(dependencies={"TS_ASST.TS_ASST_TYP"})
	def TYP_ACCNTNG_ITM(self):
		return self.TS_ASST.TS_ASST_TYP
	NN_FNNCL_ASST_NN_FNNCL_LBLTY = None # NN_FNNCL_ASST_NN_FNNCL_LBLTY
	@lineage(dependencies={"NN_FNNCL_ASST_NN_FNNCL_LBLTY.CRRYNG_AMNT"})
	def CRRYNG_AMNT(self):
		return self.NN_FNNCL_ASST_NN_FNNCL_LBLTY.CRRYNG_AMNT
	@lineage(dependencies={"NN_FNNCL_ASST_NN_FNNCL_LBLTY.NN_FNNCL_ASST_NN_FNNCL_LBLTY_TYP"})
	def TYP_ACCNTNG_ITM(self):
		return self.NN_FNNCL_ASST_NN_FNNCL_LBLTY.NN_FNNCL_ASST_NN_FNNCL_LBLTY_TYP
	NN_FNNCL_ASST = None # NN_FNNCL_ASST
	@lineage(dependencies={"NN_FNNCL_ASST.NN_FNNCL_ASST_TYP"})
	def TYP_ACCNTNG_ITM(self):
		return self.NN_FNNCL_ASST.NN_FNNCL_ASST_TYP

class Tangible_assets(F_01_01_REF_FINREP_3_0_Base):
	INVSTMNT_PRPRTY = None # INVSTMNT_PRPRTY
	@lineage(dependencies={"INVSTMNT_PRPRTY.HLD_SL_INDCTR"})
	def HLD_SL_INDCTR(self):
		return self.INVSTMNT_PRPRTY.HLD_SL_INDCTR
	NN_FNNCL_ASST = None # NN_FNNCL_ASST
	@lineage(dependencies={"NN_FNNCL_ASST.NN_FNNCL_ASST_TYP"})
	def TYP_ACCNTNG_ITM(self):
		return self.NN_FNNCL_ASST.NN_FNNCL_ASST_TYP
	NN_FNNCL_ASST_NN_FNNCL_LBLTY = None # NN_FNNCL_ASST_NN_FNNCL_LBLTY
	@lineage(dependencies={"NN_FNNCL_ASST_NN_FNNCL_LBLTY.CRRYNG_AMNT"})
	def CRRYNG_AMNT(self):
		return self.NN_FNNCL_ASST_NN_FNNCL_LBLTY.CRRYNG_AMNT
	@lineage(dependencies={"NN_FNNCL_ASST_NN_FNNCL_LBLTY.NN_FNNCL_ASST_NN_FNNCL_LBLTY_TYP"})
	def TYP_ACCNTNG_ITM(self):
		return self.NN_FNNCL_ASST_NN_FNNCL_LBLTY.NN_FNNCL_ASST_NN_FNNCL_LBLTY_TYP

class Intangible_assets_other_than_Goodwill(F_01_01_REF_FINREP_3_0_Base):
	INVSTMNT_PRPRTY = None # INVSTMNT_PRPRTY
	@lineage(dependencies={"INVSTMNT_PRPRTY.HLD_SL_INDCTR"})
	def HLD_SL_INDCTR(self):
		return self.INVSTMNT_PRPRTY.HLD_SL_INDCTR
	NN_FNNCL_ASST = None # NN_FNNCL_ASST
	@lineage(dependencies={"NN_FNNCL_ASST.NN_FNNCL_ASST_TYP"})
	def TYP_ACCNTNG_ITM(self):
		return self.NN_FNNCL_ASST.NN_FNNCL_ASST_TYP
	NN_FNNCL_ASST_NN_FNNCL_LBLTY = None # NN_FNNCL_ASST_NN_FNNCL_LBLTY
	@lineage(dependencies={"NN_FNNCL_ASST_NN_FNNCL_LBLTY.CRRYNG_AMNT"})
	def CRRYNG_AMNT(self):
		return self.NN_FNNCL_ASST_NN_FNNCL_LBLTY.CRRYNG_AMNT
	@lineage(dependencies={"NN_FNNCL_ASST_NN_FNNCL_LBLTY.NN_FNNCL_ASST_NN_FNNCL_LBLTY_TYP"})
	def TYP_ACCNTNG_ITM(self):
		return self.NN_FNNCL_ASST_NN_FNNCL_LBLTY.NN_FNNCL_ASST_NN_FNNCL_LBLTY_TYP

class Tax_assets(F_01_01_REF_FINREP_3_0_Base):
	TS_ASST = None # TS_ASST
	@lineage(dependencies={"TS_ASST.HLD_SL_INDCTR"})
	def HLD_SL_INDCTR(self):
		return self.TS_ASST.HLD_SL_INDCTR
	@lineage(dependencies={"TS_ASST.TS_ASST_TYP"})
	def TYP_ACCNTNG_ITM(self):
		return self.TS_ASST.TS_ASST_TYP
	NN_FNNCL_ASST = None # NN_FNNCL_ASST
	@lineage(dependencies={"NN_FNNCL_ASST.NN_FNNCL_ASST_TYP"})
	def TYP_ACCNTNG_ITM(self):
		return self.NN_FNNCL_ASST.NN_FNNCL_ASST_TYP
	NN_FNNCL_ASST_NN_FNNCL_LBLTY = None # NN_FNNCL_ASST_NN_FNNCL_LBLTY
	@lineage(dependencies={"NN_FNNCL_ASST_NN_FNNCL_LBLTY.CRRYNG_AMNT"})
	def CRRYNG_AMNT(self):
		return self.NN_FNNCL_ASST_NN_FNNCL_LBLTY.CRRYNG_AMNT
	@lineage(dependencies={"NN_FNNCL_ASST_NN_FNNCL_LBLTY.NN_FNNCL_ASST_NN_FNNCL_LBLTY_TYP"})
	def TYP_ACCNTNG_ITM(self):
		return self.NN_FNNCL_ASST_NN_FNNCL_LBLTY.NN_FNNCL_ASST_NN_FNNCL_LBLTY_TYP

class Tangible_assets_Investment_property(F_01_01_REF_FINREP_3_0_Base):
	INVSTMNT_PRPRTY = None # INVSTMNT_PRPRTY
	@lineage(dependencies={"INVSTMNT_PRPRTY.HLD_SL_INDCTR"})
	def HLD_SL_INDCTR(self):
		return self.INVSTMNT_PRPRTY.HLD_SL_INDCTR
	NN_FNNCL_ASST = None # NN_FNNCL_ASST
	@lineage(dependencies={"NN_FNNCL_ASST.NN_FNNCL_ASST_TYP"})
	def TYP_ACCNTNG_ITM(self):
		return self.NN_FNNCL_ASST.NN_FNNCL_ASST_TYP
	NN_FNNCL_ASST_NN_FNNCL_LBLTY = None # NN_FNNCL_ASST_NN_FNNCL_LBLTY
	@lineage(dependencies={"NN_FNNCL_ASST_NN_FNNCL_LBLTY.CRRYNG_AMNT"})
	def CRRYNG_AMNT(self):
		return self.NN_FNNCL_ASST_NN_FNNCL_LBLTY.CRRYNG_AMNT
	@lineage(dependencies={"NN_FNNCL_ASST_NN_FNNCL_LBLTY.NN_FNNCL_ASST_NN_FNNCL_LBLTY_TYP"})
	def TYP_ACCNTNG_ITM(self):
		return self.NN_FNNCL_ASST_NN_FNNCL_LBLTY.NN_FNNCL_ASST_NN_FNNCL_LBLTY_TYP

class Current_tax_assets(F_01_01_REF_FINREP_3_0_Base):
	TS_ASST = None # TS_ASST
	@lineage(dependencies={"TS_ASST.HLD_SL_INDCTR"})
	def HLD_SL_INDCTR(self):
		return self.TS_ASST.HLD_SL_INDCTR
	@lineage(dependencies={"TS_ASST.TS_ASST_TYP"})
	def TYP_ACCNTNG_ITM(self):
		return self.TS_ASST.TS_ASST_TYP
	NN_FNNCL_ASST_NN_FNNCL_LBLTY = None # NN_FNNCL_ASST_NN_FNNCL_LBLTY
	@lineage(dependencies={"NN_FNNCL_ASST_NN_FNNCL_LBLTY.CRRYNG_AMNT"})
	def CRRYNG_AMNT(self):
		return self.NN_FNNCL_ASST_NN_FNNCL_LBLTY.CRRYNG_AMNT
	@lineage(dependencies={"NN_FNNCL_ASST_NN_FNNCL_LBLTY.NN_FNNCL_ASST_NN_FNNCL_LBLTY_TYP"})
	def TYP_ACCNTNG_ITM(self):
		return self.NN_FNNCL_ASST_NN_FNNCL_LBLTY.NN_FNNCL_ASST_NN_FNNCL_LBLTY_TYP
	NN_FNNCL_ASST = None # NN_FNNCL_ASST
	@lineage(dependencies={"NN_FNNCL_ASST.NN_FNNCL_ASST_TYP"})
	def TYP_ACCNTNG_ITM(self):
		return self.NN_FNNCL_ASST.NN_FNNCL_ASST_TYP

class F_01_01_REF_FINREP_3_0_Equity_instruments_Table:
	EQTY_FND_SCRTY_Table = None # EQTY_FND_SCRTY
	LNG_EQUTY_FND_SCRTY_PSTN_PRDNTL_PRFL_ASSGNMNT_ACCNTNG_CLSSFCTN_ASST_ASSGNMNT_IFRS_Table = None # LNG_EQUTY_FND_SCRTY_PSTN_PRDNTL_PRFL_ASSGNMNT_ACCNTNG_CLSSFCTN_ASST_ASSGNMNT_IFRS
	LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FR_FNNCL_ASSTS_ASSGNMNT_DRVD_DT_Table = None # LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FR_FNNCL_ASSTS_ASSGNMNT_DRVD_DT
	LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASSTS_ASSGNMNT_Table = None # LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASSTS_ASSGNMNT
	LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_Table = None # LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT
	SCRTY_PSTN_Table = None # SCRTY_PSTN
	LNG_SCRTY_PSTN_HDG_Table = None # LNG_SCRTY_PSTN_HDG
	LNG_SCRTY_PSTN_DRVD_DT_Table = None # LNG_SCRTY_PSTN_DRVD_DT
	SCRTY_Table = None # SCRTY
	SCRTY_ISSR_ASSGNMNT_Table = None # SCRTY_ISSR_ASSGNMNT
	PRTY_RL_Table = None # PRTY_RL
	ENTTY_RL_Table = None # ENTTY_RL
	ENTTY_TRNSCTN_RL_Table = None # ENTTY_TRNSCTN_RL
	PRTY_Table = None # PRTY
	PRTY_DRVD_DT_Table = None # PRTY_DRVD_DT
	SCRTY_EXCHNG_TRDBL_DRVTV_Table = None # SCRTY_EXCHNG_TRDBL_DRVTV
	Equity_instrumentss = []# Equity_instruments[]
	def calc_Equity_instrumentss(self) :
		items = [] # Equity_instruments[
		# Join up any refered tables that you need to join
		# loop through the main table
		# set any references you want to on the new Item so that it can refer to themin operations
		return items
	def init(self):
		Orchestration().init(self)
		self.Equity_instrumentss = []
		self.Equity_instrumentss.extend(self.calc_Equity_instrumentss())
		CSVConverter.persist_object_as_csv(self,True)
		return None


class F_01_01_REF_FINREP_3_0_Debt_securities_Table:
	LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASSTS_ASSGNMNT_Table = None # LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASSTS_ASSGNMNT
	PRTY_Table = None # PRTY
	ISIN_SCRTY_Table = None # ISIN_SCRTY
	LNG_SCRTY_PSTN_HDG_Table = None # LNG_SCRTY_PSTN_HDG
	SCRTY_ISSR_ASSGNMNT_Table = None # SCRTY_ISSR_ASSGNMNT
	DBT_SCRTY_Table = None # DBT_SCRTY
	LNG_DBT_SCRTY_PSTN_PRDNTL_PRFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASSTS_ASSGNMNT_IFRS_Table = None # LNG_DBT_SCRTY_PSTN_PRDNTL_PRFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASSTS_ASSGNMNT_IFRS
	Debt_securitiess = []# Debt_securities[]
	def calc_Debt_securitiess(self) :
		items = [] # Debt_securities[
		# Join up any refered tables that you need to join
		# loop through the main table
		# set any references you want to on the new Item so that it can refer to themin operations
		return items
	def init(self):
		Orchestration().init(self)
		self.Debt_securitiess = []
		self.Debt_securitiess.extend(self.calc_Debt_securitiess())
		CSVConverter.persist_object_as_csv(self,True)
		return None


class F_01_01_REF_FINREP_3_0_Derivatives_Table:
	EXCHNG_TRDBL_DRVTV_PSTN_Table = None # EXCHNG_TRDBL_DRVTV_PSTN
	PRTY_Table = None # PRTY
	PRTY_DRVD_DT_Table = None # PRTY_DRVD_DT
	PRTY_RL_Table = None # PRTY_RL
	ENTTY_RL_Table = None # ENTTY_RL
	ENTTY_TRNSCTN_RL_Table = None # ENTTY_TRNSCTN_RL
	SCRTY_EXCHNG_TRDBL_DRVTV_Table = None # SCRTY_EXCHNG_TRDBL_DRVTV
	SCRTY_ISSR_ASSGNMNT_Table = None # SCRTY_ISSR_ASSGNMNT
	OTC_DRVTV_INSTRMNT_Table = None # OTC_DRVTV_INSTRMNT
	INSTRMNT_Table = None # INSTRMNT
	INSTRMNT_SRVCR_ASSGNMNT_Table = None # INSTRMNT_SRVCR_ASSGNMNT
	OTC_DRVTV_BUYR_ASSGNMNT_Table = None # OTC_DRVTV_BUYR_ASSGNMNT
	OTC_DRVTV_SLLR_ASSGNMNT_Table = None # OTC_DRVTV_SLLR_ASSGNMNT
	Derivativess = []# Derivatives[]
	def calc_Derivativess(self) :
		items = [] # Derivatives[
		# Join up any refered tables that you need to join
		# loop through the main table
		# set any references you want to on the new Item so that it can refer to themin operations
		return items
	def init(self):
		Orchestration().init(self)
		self.Derivativess = []
		self.Derivativess.extend(self.calc_Derivativess())
		CSVConverter.persist_object_as_csv(self,True)
		return None


class F_01_01_REF_FINREP_3_0_Intangible_assets_Goodwill_Table:
	INVSTMNT_PRPRTY_Table = None # INVSTMNT_PRPRTY
	NN_FNNCL_ASST_Table = None # NN_FNNCL_ASST
	NN_FNNCL_ASST_NN_FNNCL_LBLTY_Table = None # NN_FNNCL_ASST_NN_FNNCL_LBLTY
	Intangible_assets_Goodwills = []# Intangible_assets_Goodwill[]
	def calc_Intangible_assets_Goodwills(self) :
		items = [] # Intangible_assets_Goodwill[
		# Join up any refered tables that you need to join
		# loop through the main table
		# set any references you want to on the new Item so that it can refer to themin operations
		return items
	def init(self):
		Orchestration().init(self)
		self.Intangible_assets_Goodwills = []
		self.Intangible_assets_Goodwills.extend(self.calc_Intangible_assets_Goodwills())
		CSVConverter.persist_object_as_csv(self,True)
		return None


class F_01_01_REF_FINREP_3_0_Non_current_assets_and_disposal_groups_classified_as_held_for_sale_Table:
	INVSTMNT_PRPRTY_Table = None # INVSTMNT_PRPRTY
	NN_FNNCL_ASST_Table = None # NN_FNNCL_ASST
	NN_FNNCL_ASST_NN_FNNCL_LBLTY_Table = None # NN_FNNCL_ASST_NN_FNNCL_LBLTY
	Non_current_assets_and_disposal_groups_classified_as_held_for_sales = []# Non_current_assets_and_disposal_groups_classified_as_held_for_sale[]
	def calc_Non_current_assets_and_disposal_groups_classified_as_held_for_sales(self) :
		items = [] # Non_current_assets_and_disposal_groups_classified_as_held_for_sale[
		# Join up any refered tables that you need to join
		# loop through the main table
		# set any references you want to on the new Item so that it can refer to themin operations
		return items
	def init(self):
		Orchestration().init(self)
		self.Non_current_assets_and_disposal_groups_classified_as_held_for_sales = []
		self.Non_current_assets_and_disposal_groups_classified_as_held_for_sales.extend(self.calc_Non_current_assets_and_disposal_groups_classified_as_held_for_sales())
		CSVConverter.persist_object_as_csv(self,True)
		return None


class F_01_01_REF_FINREP_3_0_Intangible_assets_Table:
	INVSTMNT_PRPRTY_Table = None # INVSTMNT_PRPRTY
	NN_FNNCL_ASST_Table = None # NN_FNNCL_ASST
	NN_FNNCL_ASST_NN_FNNCL_LBLTY_Table = None # NN_FNNCL_ASST_NN_FNNCL_LBLTY
	Intangible_assetss = []# Intangible_assets[]
	def calc_Intangible_assetss(self) :
		items = [] # Intangible_assets[
		# Join up any refered tables that you need to join
		# loop through the main table
		# set any references you want to on the new Item so that it can refer to themin operations
		return items
	def init(self):
		Orchestration().init(self)
		self.Intangible_assetss = []
		self.Intangible_assetss.extend(self.calc_Intangible_assetss())
		CSVConverter.persist_object_as_csv(self,True)
		return None


class F_01_01_REF_FINREP_3_0_Deferred_tax_assets_Table:
	TS_ASST_Table = None # TS_ASST
	NN_FNNCL_ASST_NN_FNNCL_LBLTY_Table = None # NN_FNNCL_ASST_NN_FNNCL_LBLTY
	NN_FNNCL_ASST_Table = None # NN_FNNCL_ASST
	Deferred_tax_assetss = []# Deferred_tax_assets[]
	def calc_Deferred_tax_assetss(self) :
		items = [] # Deferred_tax_assets[
		# Join up any refered tables that you need to join
		# loop through the main table
		# set any references you want to on the new Item so that it can refer to themin operations
		return items
	def init(self):
		Orchestration().init(self)
		self.Deferred_tax_assetss = []
		self.Deferred_tax_assetss.extend(self.calc_Deferred_tax_assetss())
		CSVConverter.persist_object_as_csv(self,True)
		return None


class F_01_01_REF_FINREP_3_0_Tangible_assets_Table:
	INVSTMNT_PRPRTY_Table = None # INVSTMNT_PRPRTY
	NN_FNNCL_ASST_Table = None # NN_FNNCL_ASST
	NN_FNNCL_ASST_NN_FNNCL_LBLTY_Table = None # NN_FNNCL_ASST_NN_FNNCL_LBLTY
	Tangible_assetss = []# Tangible_assets[]
	def calc_Tangible_assetss(self) :
		items = [] # Tangible_assets[
		# Join up any refered tables that you need to join
		# loop through the main table
		# set any references you want to on the new Item so that it can refer to themin operations
		return items
	def init(self):
		Orchestration().init(self)
		self.Tangible_assetss = []
		self.Tangible_assetss.extend(self.calc_Tangible_assetss())
		CSVConverter.persist_object_as_csv(self,True)
		return None


class F_01_01_REF_FINREP_3_0_Intangible_assets_other_than_Goodwill_Table:
	INVSTMNT_PRPRTY_Table = None # INVSTMNT_PRPRTY
	NN_FNNCL_ASST_Table = None # NN_FNNCL_ASST
	NN_FNNCL_ASST_NN_FNNCL_LBLTY_Table = None # NN_FNNCL_ASST_NN_FNNCL_LBLTY
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


class F_01_01_REF_FINREP_3_0_Tax_assets_Table:
	TS_ASST_Table = None # TS_ASST
	NN_FNNCL_ASST_Table = None # NN_FNNCL_ASST
	NN_FNNCL_ASST_NN_FNNCL_LBLTY_Table = None # NN_FNNCL_ASST_NN_FNNCL_LBLTY
	Tax_assetss = []# Tax_assets[]
	def calc_Tax_assetss(self) :
		items = [] # Tax_assets[
		# Join up any refered tables that you need to join
		# loop through the main table
		# set any references you want to on the new Item so that it can refer to themin operations
		return items
	def init(self):
		Orchestration().init(self)
		self.Tax_assetss = []
		self.Tax_assetss.extend(self.calc_Tax_assetss())
		CSVConverter.persist_object_as_csv(self,True)
		return None


class F_01_01_REF_FINREP_3_0_Tangible_assets_Investment_property_Table:
	INVSTMNT_PRPRTY_Table = None # INVSTMNT_PRPRTY
	NN_FNNCL_ASST_Table = None # NN_FNNCL_ASST
	NN_FNNCL_ASST_NN_FNNCL_LBLTY_Table = None # NN_FNNCL_ASST_NN_FNNCL_LBLTY
	Tangible_assets_Investment_propertys = []# Tangible_assets_Investment_property[]
	def calc_Tangible_assets_Investment_propertys(self) :
		items = [] # Tangible_assets_Investment_property[
		# Join up any refered tables that you need to join
		# loop through the main table
		# set any references you want to on the new Item so that it can refer to themin operations
		return items
	def init(self):
		Orchestration().init(self)
		self.Tangible_assets_Investment_propertys = []
		self.Tangible_assets_Investment_propertys.extend(self.calc_Tangible_assets_Investment_propertys())
		CSVConverter.persist_object_as_csv(self,True)
		return None


class F_01_01_REF_FINREP_3_0_Current_tax_assets_Table:
	TS_ASST_Table = None # TS_ASST
	NN_FNNCL_ASST_NN_FNNCL_LBLTY_Table = None # NN_FNNCL_ASST_NN_FNNCL_LBLTY
	NN_FNNCL_ASST_Table = None # NN_FNNCL_ASST
	Current_tax_assetss = []# Current_tax_assets[]
	def calc_Current_tax_assetss(self) :
		items = [] # Current_tax_assets[
		# Join up any refered tables that you need to join
		# loop through the main table
		# set any references you want to on the new Item so that it can refer to themin operations
		return items
	def init(self):
		Orchestration().init(self)
		self.Current_tax_assetss = []
		self.Current_tax_assetss.extend(self.calc_Current_tax_assetss())
		CSVConverter.persist_object_as_csv(self,True)
		return None

