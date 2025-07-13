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
	@lineage(dependencies={"base.TYP_HDG"})
	def TYP_HDG(self) -> str:
		''' return string from TYP_HDG enumeration '''
		return self.base.TYP_HDG()
	@lineage(dependencies={"base.ACCNTNG_CLSSFCTN"})
	def ACCNTNG_CLSSFCTN(self) -> str:
		''' return string from ACCNTNG_CLSSFCTN enumeration '''
		return self.base.ACCNTNG_CLSSFCTN()
	@lineage(dependencies={"base.PRTY_RL_TYP"})
	def PRTY_RL_TYP(self) -> str:
		''' return string from ENTTY_RL_TYP enumeration '''
		return self.base.PRTY_RL_TYP()
	@lineage(dependencies={"base.HLD_SL_INDCTR"})
	def HLD_SL_INDCTR(self) -> str:
		''' return string from HLD_SL_INDCTR enumeration '''
		return self.base.HLD_SL_INDCTR()
	@lineage(dependencies={"base.INSTTTNL_SCTR"})
	def INSTTTNL_SCTR(self) -> str:
		''' return string from INSTTTNL_SCTR enumeration '''
		return self.base.INSTTTNL_SCTR()
	@lineage(dependencies={"base.MN_DBTR_INDCTR"})
	def MN_DBTR_INDCTR(self) -> str:
		''' return string from MN_DBTR_INDCTR enumeration '''
		return self.base.MN_DBTR_INDCTR()
	@lineage(dependencies={"base.RPYMNT_RGHTS"})
	def RPYMNT_RGHTS(self) -> str:
		''' return string from RPYMNT_RGHTS enumeration '''
		return self.base.RPYMNT_RGHTS()
	@lineage(dependencies={"base.SBJCT_IMPRMNT_INDCTR"})
	def SBJCT_IMPRMNT_INDCTR(self) -> str:
		''' return string from SBJCT_IMPRMNT_INDCTR enumeration '''
		return self.base.SBJCT_IMPRMNT_INDCTR()
	@lineage(dependencies={"base.TYP_INSTRMNT"})
	def TYP_INSTRMNT(self) -> str:
		''' return string from TYP_INSTRMNT enumeration '''
		return self.base.TYP_INSTRMNT()
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

class F_01_01_REF_FINREP_3_0_Base:
	def CRRYNG_AMNT() -> int:
		pass
	def TYP_HDG() -> str:
		''' return string from TYP_HDG enumeration '''
		pass
	def ACCNTNG_CLSSFCTN() -> str:
		''' return string from ACCNTNG_CLSSFCTN enumeration '''
		pass
	def PRTY_RL_TYP() -> str:
		''' return string from ENTTY_RL_TYP enumeration '''
		pass
	def HLD_SL_INDCTR() -> str:
		''' return string from HLD_SL_INDCTR enumeration '''
		pass
	def INSTTTNL_SCTR() -> str:
		''' return string from INSTTTNL_SCTR enumeration '''
		pass
	def MN_DBTR_INDCTR() -> str:
		''' return string from MN_DBTR_INDCTR enumeration '''
		pass
	def RPYMNT_RGHTS() -> str:
		''' return string from RPYMNT_RGHTS enumeration '''
		pass
	def SBJCT_IMPRMNT_INDCTR() -> str:
		''' return string from SBJCT_IMPRMNT_INDCTR enumeration '''
		pass
	def TYP_INSTRMNT() -> str:
		''' return string from TYP_INSTRMNT enumeration '''
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

class F_01_01_REF_FINREP_3_0_UnionTable :
	F_01_01_REF_FINREP_3_0_UnionItems = [] # F_01_01_REF_FINREP_3_0_UnionItem []
	F_01_01_REF_FINREP_3_0_Other_loans_Table = None # Other_loans
	F_01_01_REF_FINREP_3_0_Tangible_assets_Table = None # Tangible_assets
	F_01_01_REF_FINREP_3_0_Debt_securities_Table = None # Debt_securities
	F_01_01_REF_FINREP_3_0_Non_Negotiable_bonds_Table = None # Non_Negotiable_bonds
	F_01_01_REF_FINREP_3_0_Current_tax_assets_Table = None # Current_tax_assets
	F_01_01_REF_FINREP_3_0_Deferred_tax_assets_Table = None # Deferred_tax_assets
	F_01_01_REF_FINREP_3_0_Intangible_assets_Table = None # Intangible_assets
	F_01_01_REF_FINREP_3_0_Intangible_assets_Goodwill_Table = None # Intangible_assets_Goodwill
	F_01_01_REF_FINREP_3_0_Intangible_assets_other_than_Goodwill_Table = None # Intangible_assets_other_than_Goodwill
	F_01_01_REF_FINREP_3_0_Tax_assets_Table = None # Tax_assets
	def calc_F_01_01_REF_FINREP_3_0_UnionItems(self) -> list[F_01_01_REF_FINREP_3_0_UnionItem] :
		items = [] # F_01_01_REF_FINREP_3_0_UnionItem []
		for item in self.F_01_01_REF_FINREP_3_0_Other_loans_Table.Other_loanss:
			newItem = F_01_01_REF_FINREP_3_0_UnionItem()
			newItem.base = item
			items.append(newItem)
		for item in self.F_01_01_REF_FINREP_3_0_Tangible_assets_Table.Tangible_assetss:
			newItem = F_01_01_REF_FINREP_3_0_UnionItem()
			newItem.base = item
			items.append(newItem)
		for item in self.F_01_01_REF_FINREP_3_0_Debt_securities_Table.Debt_securitiess:
			newItem = F_01_01_REF_FINREP_3_0_UnionItem()
			newItem.base = item
			items.append(newItem)
		for item in self.F_01_01_REF_FINREP_3_0_Non_Negotiable_bonds_Table.Non_Negotiable_bondss:
			newItem = F_01_01_REF_FINREP_3_0_UnionItem()
			newItem.base = item
			items.append(newItem)
		for item in self.F_01_01_REF_FINREP_3_0_Current_tax_assets_Table.Current_tax_assetss:
			newItem = F_01_01_REF_FINREP_3_0_UnionItem()
			newItem.base = item
			items.append(newItem)
		for item in self.F_01_01_REF_FINREP_3_0_Deferred_tax_assets_Table.Deferred_tax_assetss:
			newItem = F_01_01_REF_FINREP_3_0_UnionItem()
			newItem.base = item
			items.append(newItem)
		for item in self.F_01_01_REF_FINREP_3_0_Intangible_assets_Table.Intangible_assetss:
			newItem = F_01_01_REF_FINREP_3_0_UnionItem()
			newItem.base = item
			items.append(newItem)
		for item in self.F_01_01_REF_FINREP_3_0_Intangible_assets_Goodwill_Table.Intangible_assets_Goodwills:
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
		return items

	def init(self):
		Orchestration().init(self)
		self.F_01_01_REF_FINREP_3_0_UnionItems = []
		self.F_01_01_REF_FINREP_3_0_UnionItems.extend(self.calc_F_01_01_REF_FINREP_3_0_UnionItems())
		CSVConverter.persist_object_as_csv(self,True)
		return None


class Other_loans(F_01_01_REF_FINREP_3_0_Base):

	INSTRMNT = None # INSTRMNT
	def RPYMNT_RGHTS(self):
		''' return string from RPYMNT_RGHTS enumeration of 2 fro Other_than_on_demand_or_short_notice'''
		return '2'	
	@lineage(dependencies={"INSTRMNT.TYP_INSTRMNT"})
	def TYP_INSTRMNT(self):
		return self.INSTRMNT.TYP_INSTRMNT
	INSTRMNT_ENTTY_RL_ASSGNMNT = None # INSTRMNT_ENTTY_RL_ASSGNMNT
	@lineage(dependencies={"INSTRMNT_ENTTY_RL_ASSGNMNT.MN_DBTR_INDCTR"})
	def MN_DBTR_INDCTR(self):
		return self.INSTRMNT_ENTTY_RL_ASSGNMNT.MN_DBTR_INDCTR
	@lineage(dependencies={"INSTRMNT_ENTTY_RL_ASSGNMNT.PRTY_RL_TYP"})
	def PRTY_RL_TYP(self):
		return self.INSTRMNT_ENTTY_RL_ASSGNMNT.PRTY_RL_TYP
	INSTRMNT_RL = None # INSTRMNT_RL
	@lineage(dependencies={"INSTRMNT_RL.ACCNTNG_CLSSFCTN"})
	def ACCNTNG_CLSSFCTN(self):
		return self.INSTRMNT_RL.ACCNTNG_CLSSFCTN
	@lineage(dependencies={"INSTRMNT_RL.CRRYNG_AMNT"})
	def CRRYNG_AMNT(self):
		return self.INSTRMNT_RL.CRRYNG_AMNT
	@lineage(dependencies={"INSTRMNT_RL.HLD_SL_INDCTR"})
	def HLD_SL_INDCTR(self):
		return self.INSTRMNT_RL.HLD_SL_INDCTR
	@lineage(dependencies={"INSTRMNT_RL.SBJCT_IMPRMNT_INDCTR"})
	def SBJCT_IMPRMNT_INDCTR(self):
		return self.INSTRMNT_RL.SBJCT_IMPRMNT_INDCTR
	@lineage(dependencies={"INSTRMNT_RL.GRSS_CRRYNG_AMNT"})
	def GRSS_CRRYNG_AMNT(self):
		return self.INSTRMNT_RL.GRSS_CRRYNG_AMNT
	PRTY = None # PRTY
	@lineage(dependencies={"PRTY.INSTTTNL_SCTR"})
	def INSTTTNL_SCTR(self):
		return self.PRTY.INSTTTNL_SCTR
	SCRTY_EXCHNG_TRDBL_DRVTV = None # SCRTY_EXCHNG_TRDBL_DRVTV
	def NGTBL_SCRTY_INDCTR(self):
		''' return string from NGTBL_SCRTY enumeration of 2 for non-negotiable '''
		return '2'
	def TYP_HDG(self) -> str:
		''' return string from TYP_HDG enumeration '''
		return '0'
	def SCRTY_EXCHNG_TRDBL_DRVTV_TYP(self):
		return '0'
	def TYP_ACCNTNG_ITM(self):
		return '0'
	

class Tangible_assets(F_01_01_REF_FINREP_3_0_Base):
	CLLTRL = None # CLLTRL
	@lineage(dependencies={"CLLTRL.CRRYNG_AMNT"})
	def CRRYNG_AMNT(self):
		return self.CLLTRL.CRRYNG_AMNT
	CRDT_FCLTY = None # CRDT_FCLTY
	@lineage(dependencies={"CRDT_FCLTY.ACCNTNG_CLSSFCTN"})
	def ACCNTNG_CLSSFCTN(self):
		return self.CRDT_FCLTY.ACCNTNG_CLSSFCTN
	INSTRMNT = None # INSTRMNT
	@lineage(dependencies={"INSTRMNT.RPYMNT_RGHTS"})
	def RPYMNT_RGHTS(self):
		return self.INSTRMNT.RPYMNT_RGHTS
	@lineage(dependencies={"INSTRMNT.INSTRMNT_TYP_ORGN"})
	def TYP_INSTRMNT(self):
		return self.INSTRMNT.INSTRMNT_TYP_ORGN
	@lineage(dependencies={"INSTRMNT.TYP_INSTRMNT"})
	def TYP_INSTRMNT(self):
		return self.INSTRMNT.TYP_INSTRMNT
	NN_FNNCL_ASST = None # NN_FNNCL_ASST
	@lineage(dependencies={"NN_FNNCL_ASST.CRRYNG_AMNT"})
	def CRRYNG_AMNT(self):
		return self.NN_FNNCL_ASST.CRRYNG_AMNT
	@lineage(dependencies={"NN_FNNCL_ASST.HLD_SL_INDCTR"})
	def HLD_SL_INDCTR(self):
		return self.NN_FNNCL_ASST.HLD_SL_INDCTR
	@lineage(dependencies={"NN_FNNCL_ASST.TYP_NN_FNNCL_ASST"})
	def TYP_ACCNTNG_ITM(self):
		return self.NN_FNNCL_ASST.TYP_NN_FNNCL_ASST
	PRTY = None # PRTY
	@lineage(dependencies={"PRTY.INSTTNL_SCTR_EBA_ITS"})
	def INSTTTNL_SCTR(self):
		return self.PRTY.INSTTNL_SCTR_EBA_ITS
	@lineage(dependencies={"PRTY.INSTTNL_SCTR_SHS"})
	def INSTTTNL_SCTR(self):
		return self.PRTY.INSTTNL_SCTR_SHS
	@lineage(dependencies={"PRTY.INSTTTNL_SCTR"})
	def INSTTTNL_SCTR(self):
		return self.PRTY.INSTTTNL_SCTR
	SCRTY_EXCHNG_TRDBL_DRVTV = None # SCRTY_EXCHNG_TRDBL_DRVTV
	@lineage(dependencies={"SCRTY_EXCHNG_TRDBL_DRVTV.NGTBL_SCRTY_INDCTR"})
	def NGTBL_SCRTY_INDCTR(self):
		return self.SCRTY_EXCHNG_TRDBL_DRVTV.NGTBL_SCRTY_INDCTR
	@lineage(dependencies={"SCRTY_EXCHNG_TRDBL_DRVTV.DBT_SCRTY_ACCNTNG_STNDRD"})
	def SCRTY_EXCHNG_TRDBL_DRVTV_TYP(self):
		return self.SCRTY_EXCHNG_TRDBL_DRVTV.DBT_SCRTY_ACCNTNG_STNDRD
	@lineage(dependencies={"SCRTY_EXCHNG_TRDBL_DRVTV.DBT_SCRTY_PRFRMNG_STTS_TYP"})
	def SCRTY_EXCHNG_TRDBL_DRVTV_TYP(self):
		return self.SCRTY_EXCHNG_TRDBL_DRVTV.DBT_SCRTY_PRFRMNG_STTS_TYP
	@lineage(dependencies={"SCRTY_EXCHNG_TRDBL_DRVTV.PRPTL_DBT_SCRTY_INDCTR"})
	def SCRTY_EXCHNG_TRDBL_DRVTV_TYP(self):
		return self.SCRTY_EXCHNG_TRDBL_DRVTV.PRPTL_DBT_SCRTY_INDCTR
	@lineage(dependencies={"SCRTY_EXCHNG_TRDBL_DRVTV.SCRTY_TYP_BY_IDNTFR"})
	def SCRTY_EXCHNG_TRDBL_DRVTV_TYP(self):
		return self.SCRTY_EXCHNG_TRDBL_DRVTV.SCRTY_TYP_BY_IDNTFR
	@lineage(dependencies={"SCRTY_EXCHNG_TRDBL_DRVTV.TYP_SCRTY_EXCHNG_TRDBL_DRVTV"})
	def SCRTY_EXCHNG_TRDBL_DRVTV_TYP(self):
		return self.SCRTY_EXCHNG_TRDBL_DRVTV.TYP_SCRTY_EXCHNG_TRDBL_DRVTV

class Debt_securities(F_01_01_REF_FINREP_3_0_Base):
	def MN_DBTR_INDCTR(self):
		# return 1 for main debtor
		return '1'
	LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASSTS_ASSGNMNT = None # LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASSTS_ASSGNMNT
	@lineage(dependencies={"LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASSTS_ASSGNMNT.ACCNTNG_CLSSFCTN"})
	def ACCNTNG_CLSSFCTN(self):
		return self.LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASSTS_ASSGNMNT.ACCNTNG_CLSSFCTN
	@lineage(dependencies={"LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASSTS_ASSGNMNT.CRRYNG_AMNT"})
	def CRRYNG_AMNT(self):
		return self.LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASSTS_ASSGNMNT.CRRYNG_AMNT
	@lineage(dependencies={"LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASSTS_ASSGNMNT.HLD_SL_INDCTR"})
	def HLD_SL_INDCTR(self):
		return self.LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASSTS_ASSGNMNT.HLD_SL_INDCTR
	@lineage(dependencies={"LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASSTS_ASSGNMNT.SBJCT_IMPRMNT_INDCTR"})
	def SBJCT_IMPRMNT_INDCTR(self):
		return self.LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASSTS_ASSGNMNT.SBJCT_IMPRMNT_INDCTR
	PRTY = None # PRTY
	@lineage(dependencies={"PRTY.INSTTTNL_SCTR"})
	def INSTTTNL_SCTR(self):
		return self.PRTY.INSTTTNL_SCTR
	SCRTY_ENTTY_RL_ASSGNMNT = None # SCRTY_ENTTY_RL_ASSGNMNT
	@lineage(dependencies={"SCRTY_ENTTY_RL_ASSGNMNT.PRTY_RL_TYP"})
	def PRTY_RL_TYP(self):
		return self.SCRTY_ENTTY_RL_ASSGNMNT.PRTY_RL_TYP
	SCRTY_EXCHNG_TRDBL_DRVTV = None # SCRTY_EXCHNG_TRDBL_DRVTV
	@lineage(dependencies={"SCRTY_EXCHNG_TRDBL_DRVTV.NGTBL_SCRTY_INDCTR"})
	def NGTBL_SCRTY_INDCTR(self):
		return self.SCRTY_EXCHNG_TRDBL_DRVTV.NGTBL_SCRTY_INDCTR
	@lineage(dependencies={"SCRTY_EXCHNG_TRDBL_DRVTV.TYP_SCRTY_EXCHNG_TRDBL_DRVTV"})
	def SCRTY_EXCHNG_TRDBL_DRVTV_TYP(self):
		return self.SCRTY_EXCHNG_TRDBL_DRVTV.TYP_SCRTY_EXCHNG_TRDBL_DRVTV
	def TYP_HDG(self) -> str:
		''' return string from TYP_HDG enumeration '''
		return '0'
	def RPYMNT_RGHTS(self):
		''' return string from RPYMNT_RGHTS enumeration of 2 fro Other_than_on_demand_or_short_notice'''
		return '2'
	def TYP_INSTRMNT(self):
		''' return string from TYP_INSTRMNT enumeration '''
		return '210'
	def TYP_ACCNTNG_ITM(self):
		return '0'

class Non_Negotiable_bonds(F_01_01_REF_FINREP_3_0_Base):
	def MN_DBTR_INDCTR(self):
		# return 1 for main debtor
		return '1'
	LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASSTS_ASSGNMNT = None # LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASSTS_ASSGNMNT
	@lineage(dependencies={"LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASSTS_ASSGNMNT.ACCNTNG_CLSSFCTN"})
	def ACCNTNG_CLSSFCTN(self):
		return self.LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASSTS_ASSGNMNT.ACCNTNG_CLSSFCTN
	@lineage(dependencies={"LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASSTS_ASSGNMNT.CRRYNG_AMNT"})
	def CRRYNG_AMNT(self):
		return self.LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASSTS_ASSGNMNT.CRRYNG_AMNT
	@lineage(dependencies={"LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASSTS_ASSGNMNT.HLD_SL_INDCTR"})
	def HLD_SL_INDCTR(self):
		return self.LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASSTS_ASSGNMNT.HLD_SL_INDCTR
	@lineage(dependencies={"LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASSTS_ASSGNMNT.SBJCT_IMPRMNT_INDCTR"})
	def SBJCT_IMPRMNT_INDCTR(self):
		return self.LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASSTS_ASSGNMNT.SBJCT_IMPRMNT_INDCTR
	PRTY = None # PRTY
	@lineage(dependencies={"PRTY.INSTTTNL_SCTR"})
	def INSTTTNL_SCTR(self):
		return self.PRTY.INSTTTNL_SCTR
	SCRTY_ENTTY_RL_ASSGNMNT = None # SCRTY_ENTTY_RL_ASSGNMNT
	@lineage(dependencies={"SCRTY_ENTTY_RL_ASSGNMNT.PRTY_RL_TYP"})
	def PRTY_RL_TYP(self):
		return self.SCRTY_ENTTY_RL_ASSGNMNT.PRTY_RL_TYP
	SCRTY_EXCHNG_TRDBL_DRVTV = None # SCRTY_EXCHNG_TRDBL_DRVTV
	@lineage(dependencies={"SCRTY_EXCHNG_TRDBL_DRVTV.NGTBL_SCRTY_INDCTR"})
	def NGTBL_SCRTY_INDCTR(self):
		return self.SCRTY_EXCHNG_TRDBL_DRVTV.NGTBL_SCRTY_INDCTR
	@lineage(dependencies={"SCRTY_EXCHNG_TRDBL_DRVTV.TYP_SCRTY_EXCHNG_TRDBL_DRVTV"})
	def SCRTY_EXCHNG_TRDBL_DRVTV_TYP(self):
		return self.SCRTY_EXCHNG_TRDBL_DRVTV.TYP_SCRTY_EXCHNG_TRDBL_DRVTV
	def TYP_HDG(self) -> str:
		''' return string from TYP_HDG enumeration '''
		return '0'
	def RPYMNT_RGHTS(self):
		''' return string from RPYMNT_RGHTS enumeration of 2 fro Other_than_on_demand_or_short_notice'''
		return '2'
	def TYP_INSTRMNT(self):
		''' return string from TYP_INSTRMNT enumeration '''
		return '1022'
	def TYP_ACCNTNG_ITM(self):
		return '0'

class Current_tax_assets(F_01_01_REF_FINREP_3_0_Base):
	NN_FNNCL_ASST = None # NN_FNNCL_ASST
	@lineage(dependencies={"NN_FNNCL_ASST.CRRYNG_AMNT"})
	def CRRYNG_AMNT(self):
		return self.NN_FNNCL_ASST.CRRYNG_AMNT
	@lineage(dependencies={"NN_FNNCL_ASST.HLD_SL_INDCTR"})
	def HLD_SL_INDCTR(self):
		return self.NN_FNNCL_ASST.HLD_SL_INDCTR
	@lineage(dependencies={"NN_FNNCL_ASST.TYP_NN_FNNCL_ASST"})
	def TYP_ACCNTNG_ITM(self):
		return self.NN_FNNCL_ASST.TYP_NN_FNNCL_ASST

class Deferred_tax_assets(F_01_01_REF_FINREP_3_0_Base):
	NN_FNNCL_ASST = None # NN_FNNCL_ASST
	@lineage(dependencies={"NN_FNNCL_ASST.CRRYNG_AMNT"})
	def CRRYNG_AMNT(self):
		return self.NN_FNNCL_ASST.CRRYNG_AMNT
	@lineage(dependencies={"NN_FNNCL_ASST.HLD_SL_INDCTR"})
	def HLD_SL_INDCTR(self):
		return self.NN_FNNCL_ASST.HLD_SL_INDCTR
	@lineage(dependencies={"NN_FNNCL_ASST.TYP_NN_FNNCL_ASST"})
	def TYP_ACCNTNG_ITM(self):
		return self.NN_FNNCL_ASST.TYP_NN_FNNCL_ASST

class Intangible_assets(F_01_01_REF_FINREP_3_0_Base):
	NN_FNNCL_ASST = None # NN_FNNCL_ASST
	@lineage(dependencies={"NN_FNNCL_ASST.CRRYNG_AMNT"})
	def CRRYNG_AMNT(self):
		return self.NN_FNNCL_ASST.CRRYNG_AMNT
	@lineage(dependencies={"NN_FNNCL_ASST.HLD_SL_INDCTR"})
	def HLD_SL_INDCTR(self):
		return self.NN_FNNCL_ASST.HLD_SL_INDCTR
	@lineage(dependencies={"NN_FNNCL_ASST.TYP_NN_FNNCL_ASST"})
	def TYP_ACCNTNG_ITM(self):
		return self.NN_FNNCL_ASST.TYP_NN_FNNCL_ASST

class Intangible_assets_Goodwill(F_01_01_REF_FINREP_3_0_Base):
	NN_FNNCL_ASST = None # NN_FNNCL_ASST
	@lineage(dependencies={"NN_FNNCL_ASST.CRRYNG_AMNT"})
	def CRRYNG_AMNT(self):
		return self.NN_FNNCL_ASST.CRRYNG_AMNT
	@lineage(dependencies={"NN_FNNCL_ASST.HLD_SL_INDCTR"})
	def HLD_SL_INDCTR(self):
		return self.NN_FNNCL_ASST.HLD_SL_INDCTR
	@lineage(dependencies={"NN_FNNCL_ASST.TYP_NN_FNNCL_ASST"})
	def TYP_ACCNTNG_ITM(self):
		return self.NN_FNNCL_ASST.TYP_NN_FNNCL_ASST

class Intangible_assets_other_than_Goodwill(F_01_01_REF_FINREP_3_0_Base):
	NN_FNNCL_ASST = None # NN_FNNCL_ASST
	@lineage(dependencies={"NN_FNNCL_ASST.CRRYNG_AMNT"})
	def CRRYNG_AMNT(self):
		return self.NN_FNNCL_ASST.CRRYNG_AMNT
	@lineage(dependencies={"NN_FNNCL_ASST.HLD_SL_INDCTR"})
	def HLD_SL_INDCTR(self):
		return self.NN_FNNCL_ASST.HLD_SL_INDCTR
	@lineage(dependencies={"NN_FNNCL_ASST.TYP_NN_FNNCL_ASST"})
	def TYP_ACCNTNG_ITM(self):
		return self.NN_FNNCL_ASST.TYP_NN_FNNCL_ASST

class Tax_assets(F_01_01_REF_FINREP_3_0_Base):
	NN_FNNCL_ASST = None # NN_FNNCL_ASST
	@lineage(dependencies={"NN_FNNCL_ASST.CRRYNG_AMNT"})
	def CRRYNG_AMNT(self):
		return self.NN_FNNCL_ASST.CRRYNG_AMNT
	@lineage(dependencies={"NN_FNNCL_ASST.HLD_SL_INDCTR"})
	def HLD_SL_INDCTR(self):
		return self.NN_FNNCL_ASST.HLD_SL_INDCTR
	@lineage(dependencies={"NN_FNNCL_ASST.TYP_NN_FNNCL_ASST"})
	def TYP_ACCNTNG_ITM(self):
		return self.NN_FNNCL_ASST.TYP_NN_FNNCL_ASST

class F_01_01_REF_FINREP_3_0_Other_loans_Table:
	INSTRMNT_Table = None # INSTRMNT
	INSTRMNT_ENTTY_RL_ASSGNMNT_Table = None # INSTRMNT_ENTTY_RL_ASSGNMNT
	INSTRMNT_RL_Table = None # INSTRMNT_RL
	PRTY_Table = None # PRTY
	SCRTY_EXCHNG_TRDBL_DRVTV_Table = None # SCRTY_EXCHNG_TRDBL_DRVTV
	Other_loanss = []# Other_loans[]	
	
	def calc_Other_loanss(self) :
		items = [] # Other_loans[
		# Join up any refered tables that you need to join
		# loop through the main table
		# set any references you want to on the new Item so that it can refer to themin operations
		
		for instrmnt_rl in self.INSTRMNT_RL_Table:
			typeInst = instrmnt_rl.theINSTRMNT.TYP_INSTRMNT
			#if (typeInst == INSTRMNT.TYP_INSTRMNT_INPT_domain['140']) or \
			#		(typeInst == INSTRMNT.TYP_INSTRMNT_INPT_domain['1022'] ) or \
			#	(typeInst == INSTRMNT.TYP_INSTRMNT_INPT_domain['51'] ) or \
			#	(typeInst == INSTRMNT.TYP_INSTRMNT_INPT_domain['80'] ) or \
			#	(typeInst == INSTRMNT.TYP_INSTRMNT_INPT_domain['12'] ) or \
			#	(typeInst == INSTRMNT.TYP_INSTRMNT_INPT_domain['522'] ):
			if (typeInst == '1022' ):
				
				newItem = Other_loans()
				newItem.INSTRMNT_RL = instrmnt_rl
				newItem.INSTRMNT = instrmnt_rl.theINSTRMNT
				
				for era in  self.INSTRMNT_ENTTY_RL_ASSGNMNT_Table:
					inst = era.theINSTRMNT
					if (inst == newItem.INSTRMNT):
						newItem.INSTRMNT_ENTTY_RL_ASSGNMNT = era
						er = era.theENTTY_RL
						newItem.PRTY = er.thePRTY
					
				items.append(newItem)
	
		return items

	def init(self):
		Orchestration().init(self)
		self.Other_loanss = []
		self.Other_loanss.extend(self.calc_Other_loanss())
		CSVConverter.persist_object_as_csv(self,True)
		return None

class F_01_01_REF_FINREP_3_0_Tangible_assets_Table:
	CLLTRL_Table = None # CLLTRL
	CRDT_FCLTY_Table = None # CRDT_FCLTY
	INSTRMNT_Table = None # INSTRMNT
	NN_FNNCL_ASST_Table = None # NN_FNNCL_ASST
	PRTY_Table = None # PRTY
	SCRTY_EXCHNG_TRDBL_DRVTV_Table = None # SCRTY_EXCHNG_TRDBL_DRVTV
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


class F_01_01_REF_FINREP_3_0_Debt_securities_Table:
	LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASSTS_ASSGNMNT_Table = None # LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASSTS_ASSGNMNT
	LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_Table = None # LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT
	PRTY_Table = None # PRTY
	SCRTY_EXCHNG_TRDBL_DRVTV_Table = None # SCRTY_EXCHNG_TRDBL_DRVTV
	SCRTY_ENTTY_RL_ASSGNMNT_Table = None # SCRTY_ENTTY_RL_ASSGNMNT
	SCRTY_PSTN_Table = None # SCRTY_PSTN
	Debt_securitiess = []# Debt_securities[]
	
	def calc_Debt_securitiess(self) :
		items = [] # Non_Negotiable_bonds[
		for long_Security_accntng_classification in self.LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASSTS_ASSGNMNT_Table:
			long_Security_assignment = long_Security_accntng_classification.theLNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT
			scrty_position = long_Security_assignment.theSCRTY_PSTN
			scrty_exchng_trdbl_drvtv = scrty_position.theSCRTY_EXCHNG_TRDBL_DRVTV	
			new_item = Debt_securities()

			for scrty_entty_rl_assignment in self.SCRTY_ENTTY_RL_ASSGNMNT_Table:
				if scrty_entty_rl_assignment.theSCRTY_EXCHNG_TRDBL_DRVTV.SCRTY_EXCHNG_TRDBL_DRVTV_uniqueID == scrty_exchng_trdbl_drvtv.SCRTY_EXCHNG_TRDBL_DRVTV_uniqueID:
					new_item.SCRTY_ENTTY_RL_ASSGNMNT = scrty_entty_rl_assignment
					entty_rl = scrty_entty_rl_assignment.theENTTY_RL
					prty = entty_rl.thePRTY
					new_item.PRTY = prty
					break
			
			new_item.LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASSTS_ASSGNMNT = long_Security_accntng_classification
			new_item.PRTY = prty
			new_item.SCRTY_EXCHNG_TRDBL_DRVTV = scrty_exchng_trdbl_drvtv
			negotiable = scrty_exchng_trdbl_drvtv.NGTBL_SCRTY_INDCTR
			# only add if not a negotiable security
			if not(negotiable == '2'):
				items.append(new_item)
		return items
	def init(self):
		Orchestration().init(self)
		self.Debt_securitiess = []
		self.Debt_securitiess.extend(self.calc_Debt_securitiess())
		CSVConverter.persist_object_as_csv(self,True)
		return None


class F_01_01_REF_FINREP_3_0_Non_Negotiable_bonds_Table:
	LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASSTS_ASSGNMNT_Table = None # LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASSTS_ASSGNMNT
	LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_Table = None # LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT
	PRTY_Table = None # PRTY
	SCRTY_EXCHNG_TRDBL_DRVTV_Table = None # SCRTY_EXCHNG_TRDBL_DRVTV
	SCRTY_ENTTY_RL_ASSGNMNT_Table = None # SCRTY_ENTTY_RL_ASSGNMNT
	SCRTY_PSTN_Table = None # SCRTY_PSTN
	Non_Negotiable_bondss = []# Non_Negotiable_bonds[]
	
	def calc_Non_Negotiable_bondss(self) :
		items = [] # Non_Negotiable_bonds[
		for long_Security_accntng_classification in self.LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASSTS_ASSGNMNT_Table:
			long_Security_assignment = long_Security_accntng_classification.theLNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT
			scrty_position = long_Security_assignment.theSCRTY_PSTN
			scrty_exchng_trdbl_drvtv = scrty_position.theSCRTY_EXCHNG_TRDBL_DRVTV	
			new_item = Non_Negotiable_bonds()

			for scrty_entty_rl_assignment in self.SCRTY_ENTTY_RL_ASSGNMNT_Table:
				if scrty_entty_rl_assignment.theSCRTY_EXCHNG_TRDBL_DRVTV.SCRTY_EXCHNG_TRDBL_DRVTV_uniqueID == scrty_exchng_trdbl_drvtv.SCRTY_EXCHNG_TRDBL_DRVTV_uniqueID:
					new_item.SCRTY_ENTTY_RL_ASSGNMNT = scrty_entty_rl_assignment
					entty_rl = scrty_entty_rl_assignment.theENTTY_RL
					prty = entty_rl.thePRTY
					new_item.PRTY = prty
					break
			
			new_item.LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASSTS_ASSGNMNT = long_Security_accntng_classification
			new_item.PRTY = prty
			new_item.SCRTY_EXCHNG_TRDBL_DRVTV = scrty_exchng_trdbl_drvtv
			negotiable = scrty_exchng_trdbl_drvtv.NGTBL_SCRTY_INDCTR
			# only add if not a negotiable security
			if negotiable == '2':
				items.append(new_item)
		return items
	
	def init(self):
		Orchestration().init(self)
		self.Non_Negotiable_bondss = []
		self.Non_Negotiable_bondss.extend(self.calc_Non_Negotiable_bondss())
		CSVConverter.persist_object_as_csv(self,True)
		return None
	


class F_01_01_REF_FINREP_3_0_Current_tax_assets_Table:
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


class F_01_01_REF_FINREP_3_0_Deferred_tax_assets_Table:
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


class F_01_01_REF_FINREP_3_0_Intangible_assets_Table:
	NN_FNNCL_ASST_Table = None # NN_FNNCL_ASST
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


class F_01_01_REF_FINREP_3_0_Intangible_assets_Goodwill_Table:
	NN_FNNCL_ASST_Table = None # NN_FNNCL_ASST
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


class F_01_01_REF_FINREP_3_0_Intangible_assets_other_than_Goodwill_Table:
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


class F_01_01_REF_FINREP_3_0_Tax_assets_Table:
	NN_FNNCL_ASST_Table = None # NN_FNNCL_ASST
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

