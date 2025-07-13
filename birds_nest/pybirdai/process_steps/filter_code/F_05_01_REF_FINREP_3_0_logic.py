from pybirdai.bird_data_model import *
from pybirdai.process_steps.pybird.orchestration import Orchestration
from pybirdai.process_steps.pybird.csv_converter import CSVConverter
from datetime import datetime
from pybirdai.annotations.decorators import lineage

class F_05_01_REF_FINREP_3_0_UnionItem:
	base = None #F_05_01_REF_FINREP_3_0_Base
	@lineage(dependencies={"base.GRSS_CRRYNG_AMNT"})
	def GRSS_CRRYNG_AMNT(self) -> int:
		return self.base.GRSS_CRRYNG_AMNT()
	@lineage(dependencies={"base.TYP_CLLTRL"})
	def TYP_CLLTRL(self) -> str:
		''' return string from TYP_PRTCTN enumeration '''
		return self.base.TYP_CLLTRL()
	@lineage(dependencies={"base.PRPS"})
	def PRPS(self) -> str:
		''' return string from PRPS enumeration '''
		return self.base.PRPS()
	@lineage(dependencies={"base.ACCNTNG_CLSSFCTN"})
	def ACCNTNG_CLSSFCTN(self) -> str:
		''' return string from ACCNTNG_CLSSFCTN enumeration '''
		return self.base.ACCNTNG_CLSSFCTN()
	@lineage(dependencies={"base.HLD_SL_INDCTR"})
	def HLD_SL_INDCTR(self) -> str:
		''' return string from HLD_SL_INDCTR enumeration '''
		return self.base.HLD_SL_INDCTR()
	@lineage(dependencies={"base.SBJCT_IMPRMNT_INDCTR"})
	def SBJCT_IMPRMNT_INDCTR(self) -> str:
		''' return string from SBJCT_IMPRMNT_INDCTR enumeration '''
		return self.base.SBJCT_IMPRMNT_INDCTR()
	@lineage(dependencies={"base.INSTTTNL_SCTR"})
	def INSTTTNL_SCTR(self) -> str:
		''' return string from INSTTTNL_SCTR enumeration '''
		return self.base.INSTTTNL_SCTR()
	@lineage(dependencies={"base.MLTLTRL_DVLPMNT_BNK_INDCTR"})
	def MLTLTRL_DVLPMNT_BNK_INDCTR(self) -> str:
		''' return string from MLTLTRL_DVLPMNT_BNK_INDCTR enumeration '''
		return self.base.MLTLTRL_DVLPMNT_BNK_INDCTR()
	@lineage(dependencies={"base.PRTY_RL_TYP"})
	def PRTY_RL_TYP(self) -> str:
		''' return string from ENTTY_RL_TYP enumeration '''
		return self.base.PRTY_RL_TYP()
	@lineage(dependencies={"base.MN_DBTR_INDCTR"})
	def MN_DBTR_INDCTR(self) -> str:
		''' return string from MN_DBTR_INDCTR enumeration '''
		return self.base.MN_DBTR_INDCTR()
	@lineage(dependencies={"base.TYP_INSTRMNT"})
	def TYP_INSTRMNT(self) -> str:
		''' return string from TYP_INSTRMNT enumeration '''
		return self.base.TYP_INSTRMNT()
	@lineage(dependencies={"base.RPYMNT_RGHTS"})
	def RPYMNT_RGHTS(self) -> str:
		''' return string from RPYMNT_RGHTS enumeration '''
		return self.base.RPYMNT_RGHTS()
	@lineage(dependencies={"base.PRJCT_FNNC_LN"})
	def PRJCT_FNNC_LN(self) -> str:
		''' return string from PRJCT_FNNC_LN enumeration '''
		return self.base.PRJCT_FNNC_LN()
	@lineage(dependencies={"base.NGTBL_SCRTY_INDCTR"})
	def NGTBL_SCRTY_INDCTR(self) -> str:
		''' return string from NGTBL_SCRTY enumeration '''
		return self.base.NGTBL_SCRTY_INDCTR()
	@lineage(dependencies={"base.CRRYNG_AMNT"})
	def CRRYNG_AMNT(self) -> int:
		return self.base.CRRYNG_AMNT()

class F_05_01_REF_FINREP_3_0_Base:
	def GRSS_CRRYNG_AMNT() -> int:
		pass
	def TYP_CLLTRL() -> str:
		''' return string from TYP_PRTCTN enumeration '''
		pass
	def PRPS() -> str:
		''' return string from PRPS enumeration '''
		pass
	def ACCNTNG_CLSSFCTN() -> str:
		''' return string from ACCNTNG_CLSSFCTN enumeration '''
		pass
	def HLD_SL_INDCTR() -> str:
		''' return string from HLD_SL_INDCTR enumeration '''
		pass
	def SBJCT_IMPRMNT_INDCTR() -> str:
		''' return string from SBJCT_IMPRMNT_INDCTR enumeration '''
		pass
	def INSTTTNL_SCTR() -> str:
		''' return string from INSTTTNL_SCTR enumeration '''
		pass
	def MLTLTRL_DVLPMNT_BNK_INDCTR() -> str:
		''' return string from MLTLTRL_DVLPMNT_BNK_INDCTR enumeration '''
		pass
	def PRTY_RL_TYP() -> str:
		''' return string from ENTTY_RL_TYP enumeration '''
		pass
	def MN_DBTR_INDCTR() -> str:
		''' return string from MN_DBTR_INDCTR enumeration '''
		pass
	def TYP_INSTRMNT() -> str:
		''' return string from TYP_INSTRMNT enumeration '''
		pass
	def RPYMNT_RGHTS() -> str:
		''' return string from RPYMNT_RGHTS enumeration '''
		pass
	def PRJCT_FNNC_LN() -> str:
		''' return string from PRJCT_FNNC_LN enumeration '''
		pass
	def NGTBL_SCRTY_INDCTR() -> str:
		''' return string from NGTBL_SCRTY enumeration '''
		pass
	def CRRYNG_AMNT() -> int:
		pass

class F_05_01_REF_FINREP_3_0_UnionTable :
	F_05_01_REF_FINREP_3_0_UnionItems = [] # F_05_01_REF_FINREP_3_0_UnionItem []
	F_05_01_REF_FINREP_3_0_Credit_card_debt_Table = None # Credit_card_debt
	F_05_01_REF_FINREP_3_0_Finance_leases_Table = None # Finance_leases
	F_05_01_REF_FINREP_3_0_Other_loans_Table = None # Other_loans
	F_05_01_REF_FINREP_3_0_Trade_receivables_Table = None # Trade_receivables
	F_05_01_REF_FINREP_3_0_Non_Negotiable_bonds_Table = None # Non_Negotiable_bonds
	def calc_F_05_01_REF_FINREP_3_0_UnionItems(self) -> list[F_05_01_REF_FINREP_3_0_UnionItem] :
		items = [] # F_05_01_REF_FINREP_3_0_UnionItem []
		for item in self.F_05_01_REF_FINREP_3_0_Credit_card_debt_Table.Credit_card_debts:
			newItem = F_05_01_REF_FINREP_3_0_UnionItem()
			newItem.base = item
			items.append(newItem)
		for item in self.F_05_01_REF_FINREP_3_0_Finance_leases_Table.Finance_leasess:
			newItem = F_05_01_REF_FINREP_3_0_UnionItem()
			newItem.base = item
			items.append(newItem)
		for item in self.F_05_01_REF_FINREP_3_0_Other_loans_Table.Other_loanss:
			newItem = F_05_01_REF_FINREP_3_0_UnionItem()
			newItem.base = item
			items.append(newItem)
		for item in self.F_05_01_REF_FINREP_3_0_Trade_receivables_Table.Trade_receivabless:
			newItem = F_05_01_REF_FINREP_3_0_UnionItem()
			newItem.base = item
			items.append(newItem)
		for item in self.F_05_01_REF_FINREP_3_0_Non_Negotiable_bonds_Table.Non_Negotiable_bondss:
			newItem = F_05_01_REF_FINREP_3_0_UnionItem()
			newItem.base = item
			items.append(newItem)
		return items

	def init(self):
		Orchestration().init(self)
		self.F_05_01_REF_FINREP_3_0_UnionItems = []
		self.F_05_01_REF_FINREP_3_0_UnionItems.extend(self.calc_F_05_01_REF_FINREP_3_0_UnionItems())
		CSVConverter.persist_object_as_csv(self,True)
		return None


class Credit_card_debt(F_05_01_REF_FINREP_3_0_Base):
	CLLTRL = None # CLLTRL
	@lineage(dependencies={"CLLTRL.TYP_CLLTRL"})
	def TYP_CLLTRL(self):
		if self.CLLTRL is not None:
			return self.CLLTRL.TYP_CLLTRL
		return '0'
	pass
	pass
	INSTRMNT = None # INSTRMNT
	def NGTBL_SCRTY_INDCTR(self):
		''' return string from NGTBL_SCRTY enumeration of 2 for non-negotiable '''
		return '2'
	def RPYMNT_RGHTS(self):
		''' return string from RPYMNT_RGHTS enumeration of 2 fro Other_than_on_demand_or_short_notice'''
		return '2'	
	def MN_DBTR_INDCTR(self):
		# return 1 for main debtor
		return '1'
	@lineage(dependencies={"INSTRMNT.TYP_INSTRMNT"})
	def TYP_INSTRMNT(self):
		return self.INSTRMNT.TYP_INSTRMNT
	INSTRMNT_ENTTY_RL_ASSGNMNT = None # INSTRMNT_ENTTY_RL_ASSGNMNT
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
	@lineage(dependencies={"INSTRMNT_RL.PRJCT_FNNC_LN"})
	def PRJCT_FNNC_LN(self):
		return self.INSTRMNT_RL.PRJCT_FNNC_LN
	@lineage(dependencies={"INSTRMNT_RL.PRPS"})
	def PRPS(self):
		return self.INSTRMNT_RL.PRPS
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
	@lineage(dependencies={"PRTY.MLTLTRL_DVLPMNT_BNK_INDCTR"})
	def MLTLTRL_DVLPMNT_BNK_INDCTR(self):
		return self.PRTY.MLTLTRL_DVLPMNT_BNK_INDCTR


class Finance_leases(F_05_01_REF_FINREP_3_0_Base):
	CLLTRL = None # CLLTRL
	@lineage(dependencies={"CLLTRL.TYP_CLLTRL"})
	def TYP_CLLTRL(self):
		if self.CLLTRL is not None:
			return self.CLLTRL.TYP_CLLTRL
		return '0'
	pass
	pass
	INSTRMNT = None # INSTRMNT
	@lineage(dependencies={"INSTRMNT.RPYMNT_RGHTS"})
	def RPYMNT_RGHTS(self):
		return self.INSTRMNT.RPYMNT_RGHTS
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
	@lineage(dependencies={"INSTRMNT_RL.PRJCT_FNNC_LN"})
	def PRJCT_FNNC_LN(self):
		return self.INSTRMNT_RL.PRJCT_FNNC_LN
	@lineage(dependencies={"INSTRMNT_RL.PRPS"})
	def PRPS(self):
		return self.INSTRMNT_RL.PRPS
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
	@lineage(dependencies={"PRTY.MLTLTRL_DVLPMNT_BNK_INDCTR"})
	def MLTLTRL_DVLPMNT_BNK_INDCTR(self):
		return self.PRTY.MLTLTRL_DVLPMNT_BNK_INDCTR
	SCRTY_EXCHNG_TRDBL_DRVTV = None # SCRTY_EXCHNG_TRDBL_DRVTV
	@lineage(dependencies={"SCRTY_EXCHNG_TRDBL_DRVTV.NGTBL_SCRTY_INDCTR"})
	def NGTBL_SCRTY_INDCTR(self):
		return self.SCRTY_EXCHNG_TRDBL_DRVTV.NGTBL_SCRTY_INDCTR

class Other_loans(F_05_01_REF_FINREP_3_0_Base):
	CLLTRL = None # CLLTRL
	@lineage(dependencies={"CLLTRL.TYP_CLLTRL"})
	def TYP_CLLTRL(self):
		if self.CLLTRL is not None:
			return self.CLLTRL.TYP_CLLTRL
		return '0'
	
	INSTRMNT = None # INSTRMNT
	def NGTBL_SCRTY_INDCTR(self):
		''' return string from NGTBL_SCRTY enumeration of 2 for non-negotiable '''
		return '2'
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
	@lineage(dependencies={"INSTRMNT_RL.PRJCT_FNNC_LN"})
	def PRJCT_FNNC_LN(self):
		return self.INSTRMNT_RL.PRJCT_FNNC_LN
	@lineage(dependencies={"INSTRMNT_RL.PRPS"})
	def PRPS(self):
		return self.INSTRMNT_RL.PRPS
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
	@lineage(dependencies={"PRTY.MLTLTRL_DVLPMNT_BNK_INDCTR"})
	def MLTLTRL_DVLPMNT_BNK_INDCTR(self):
		return self.PRTY.MLTLTRL_DVLPMNT_BNK_INDCTR
	

class Trade_receivables(F_05_01_REF_FINREP_3_0_Base):
	CLLTRL = None # CLLTRL
	def TYP_CLLTRL(self):
		if self.CLLTRL is not None:
			return self.CLLTRL.TYP_CLLTRL
		return '0'
	INSTRMNT = None # INSTRMNT
	def NGTBL_SCRTY_INDCTR(self):
		''' return string from NGTBL_SCRTY enumeration of 2 for non-negotiable '''
		return '2'
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
	@lineage(dependencies={"INSTRMNT_RL.PRJCT_FNNC_LN"})
	def PRJCT_FNNC_LN(self):
		return self.INSTRMNT_RL.PRJCT_FNNC_LN
	@lineage(dependencies={"INSTRMNT_RL.PRPS"})
	def PRPS(self):
		return self.INSTRMNT_RL.PRPS
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
	@lineage(dependencies={"PRTY.MLTLTRL_DVLPMNT_BNK_INDCTR"})
	def MLTLTRL_DVLPMNT_BNK_INDCTR(self):
		return self.PRTY.MLTLTRL_DVLPMNT_BNK_INDCTR


class Non_Negotiable_bonds(F_05_01_REF_FINREP_3_0_Base):
	def PRPS(self):
		return '19'
	def RPYMNT_RGHTS(self):
		''' return string from RPYMNT_RGHTS enumeration '''
		return '2'
	def TYP_INSTRMNT(self):
		''' return string from TYP_INSTRMNT enumeration '''
		return '1022'
	def PRJCT_FNNC_LN(self):
		''' return string from PRJCT_FNNC_LN enumeration '''
		return '2'
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
	@lineage(dependencies={"LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASSTS_ASSGNMNT.GRSS_CRRYNG_AMNT"})
	def GRSS_CRRYNG_AMNT(self):
		return self.LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASSTS_ASSGNMNT.GRSS_CRRYNG_AMNT
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
	@lineage(dependencies={"PRTY.MLTLTRL_DVLPMNT_BNK_INDCTR"})
	def MLTLTRL_DVLPMNT_BNK_INDCTR(self):
		return self.PRTY.MLTLTRL_DVLPMNT_BNK_INDCTR
	SCRTY_ENTTY_RL_ASSGNMNT = None # SCRTY_ENTTY_RL_ASSGNMNT
	@lineage(dependencies={"SCRTY_ENTTY_RL_ASSGNMNT.PRTY_RL_TYP"})
	def PRTY_RL_TYP(self):
		return self.SCRTY_ENTTY_RL_ASSGNMNT.PRTY_RL_TYP
	SCRTY_EXCHNG_TRDBL_DRVTV = None # SCRTY_EXCHNG_TRDBL_DRVTV
	@lineage(dependencies={"SCRTY_EXCHNG_TRDBL_DRVTV.NGTBL_SCRTY_INDCTR"})
	def NGTBL_SCRTY_INDCTR(self):
		return self.SCRTY_EXCHNG_TRDBL_DRVTV.NGTBL_SCRTY_INDCTR
	pass


class F_05_01_REF_FINREP_3_0_Credit_card_debt_Table:
	CLLTRL_Table = None # CLLTRL
	INSTRMNT_Table = None # INSTRMNT
	INSTRMNT_ENTTY_RL_ASSGNMNT_Table = None # INSTRMNT_ENTTY_RL_ASSGNMNT
	INSTRMNT_RL_Table = None # INSTRMNT_RL
	PRTY_Table = None # PRTY
	SCRTY_EXCHNG_TRDBL_DRVTV_Table = None # SCRTY_EXCHNG_TRDBL_DRVTV
	Credit_card_debts = []# Credit_card_debt[]
	def calc_Credit_card_debts(self) :
		items = [] # 
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
			if (typeInst == '51' ):
				
				newItem = Credit_card_debt()
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
		self.Credit_card_debts = []
		self.Credit_card_debts.extend(self.calc_Credit_card_debts())
		CSVConverter.persist_object_as_csv(self,True)
		return None


class F_05_01_REF_FINREP_3_0_Finance_leases_Table:
	CLLTRL_Table = None # CLLTRL
	INSTRMNT_Table = None # INSTRMNT
	INSTRMNT_ENTTY_RL_ASSGNMNT_Table = None # INSTRMNT_ENTTY_RL_ASSGNMNT
	INSTRMNT_RL_Table = None # INSTRMNT_RL
	PRTY_Table = None # PRTY
	SCRTY_EXCHNG_TRDBL_DRVTV_Table = None # SCRTY_EXCHNG_TRDBL_DRVTV
	Finance_leasess = []# Finance_leases[]
	def calc_Finance_leasess(self) :
		items = [] # 
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
			if (typeInst == '80' ):
				
				newItem = Finance_leases()
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
		self.Finance_leasess = []
		self.Finance_leasess.extend(self.calc_Finance_leasess())
		CSVConverter.persist_object_as_csv(self,True)
		return None


class F_05_01_REF_FINREP_3_0_Other_loans_Table:
	CLLTRL_Table = None # CLLTRL
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


class F_05_01_REF_FINREP_3_0_Trade_receivables_Table:
	CLLTRL_Table = None # CLLTRL
	INSTRMNT_Table = None # INSTRMNT
	INSTRMNT_ENTTY_RL_ASSGNMNT_Table = None # INSTRMNT_ENTTY_RL_ASSGNMNT
	INSTRMNT_RL_Table = None # INSTRMNT_RL
	PRTY_Table = None # PRTY
	SCRTY_EXCHNG_TRDBL_DRVTV_Table = None # SCRTY_EXCHNG_TRDBL_DRVTV
	Other_loanss = []# Other_loans[]	
	
	def calc_Trade_receivabless(self) :
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
			if (typeInst == '1023' ):
				
				newItem = Trade_receivables()
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
		self.Trade_receivabless = []
		self.Trade_receivabless.extend(self.calc_Trade_receivabless())
		CSVConverter.persist_object_as_csv(self,True)
		return None
	
class F_05_01_REF_FINREP_3_0_Non_Negotiable_bonds_Table:
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
