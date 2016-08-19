# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: step1 --filein dbs:/SUSYGluGluToBBHToBB_M-100_TuneCUETP8M1_13TeV-pythia8/*/AODSIM --fileout file:HIG-RunIISpring16MiniAODv2-01205.root --mc --eventcontent MINIAODSIM --runUnscheduled --datatier MINIAODSIM --conditions 80X_mcRun2_asymptotic_v14 --step PAT --era Run2_2016 --no_exec
import FWCore.ParameterSet.Config as cms

from Configuration.StandardSequences.Eras import eras

process = cms.Process('PAT',eras.Run2_2016)

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('PhysicsTools.PatAlgos.slimming.metFilterPaths_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(1)
)

# Input source
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring('/store/mc/RunIIFall15DR76/SUSYGluGluToBBHToBB_M-100_TuneCUETP8M1_13TeV-pythia8/AODSIM/PU25nsData2015v1Raw_76X_mcRun2_asymptotic_v12-v1/00000/5CB5EC6E-87C4-E511-B58D-485B39897231.root', 
        '/store/mc/RunIIFall15DR76/SUSYGluGluToBBHToBB_M-100_TuneCUETP8M1_13TeV-pythia8/AODSIM/PU25nsData2015v1Raw_76X_mcRun2_asymptotic_v12-v1/00000/C821C694-87C4-E511-B2B1-001EC9B21425.root', 
        '/store/mc/RunIIFall15DR76/SUSYGluGluToBBHToBB_M-100_TuneCUETP8M1_13TeV-pythia8/AODSIM/PU25nsData2015v1Raw_76X_mcRun2_asymptotic_v12-v1/00000/CE0BFDDC-3CC3-E511-A792-20CF305B04D6.root', 
        '/store/mc/RunIIFall15DR76/SUSYGluGluToBBHToBB_M-100_TuneCUETP8M1_13TeV-pythia8/AODSIM/PU25nsData2015v1Raw_76X_mcRun2_asymptotic_v12-v1/10000/08E2F809-27C3-E511-9A64-002590D60072.root', 
        '/store/mc/RunIIFall15DR76/SUSYGluGluToBBHToBB_M-100_TuneCUETP8M1_13TeV-pythia8/AODSIM/PU25nsData2015v1Raw_76X_mcRun2_asymptotic_v12-v1/10000/26DA8B1B-FDC3-E511-B33D-485B3989725F.root', 
        '/store/mc/RunIIFall15DR76/SUSYGluGluToBBHToBB_M-100_TuneCUETP8M1_13TeV-pythia8/AODSIM/PU25nsData2015v1Raw_76X_mcRun2_asymptotic_v12-v1/10000/42787625-31C3-E511-9375-002590D6002C.root', 
        '/store/mc/RunIIFall15DR76/SUSYGluGluToBBHToBB_M-100_TuneCUETP8M1_13TeV-pythia8/AODSIM/PU25nsData2015v1Raw_76X_mcRun2_asymptotic_v12-v1/10000/A40F0BF7-A2C4-E511-B40F-1CC1DE18D4B6.root', 
        '/store/mc/RunIIFall15DR76/SUSYGluGluToBBHToBB_M-100_TuneCUETP8M1_13TeV-pythia8/AODSIM/PU25nsData2015v1Raw_76X_mcRun2_asymptotic_v12-v1/10000/D67C95C3-A2C4-E511-9AC1-485B39897231.root', 
        '/store/mc/RunIIFall15DR76/SUSYGluGluToBBHToBB_M-100_TuneCUETP8M1_13TeV-pythia8/AODSIM/PU25nsData2015v1Raw_76X_mcRun2_asymptotic_v12-v1/20000/02CD95AC-2FC3-E511-8271-D4AE526A03AD.root', 
        '/store/mc/RunIIFall15DR76/SUSYGluGluToBBHToBB_M-100_TuneCUETP8M1_13TeV-pythia8/AODSIM/PU25nsData2015v1Raw_76X_mcRun2_asymptotic_v12-v1/20000/287723C8-38C3-E511-BB0E-D4AE526A0419.root'),
    secondaryFileNames = cms.untracked.vstring()
)

process.options = cms.untracked.PSet(
    allowUnscheduled = cms.untracked.bool(True)
)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('step1 nevts:1'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition

process.MINIAODSIMoutput = cms.OutputModule("PoolOutputModule",
    compressionAlgorithm = cms.untracked.string('LZMA'),
    compressionLevel = cms.untracked.int32(4),
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('MINIAODSIM'),
        filterName = cms.untracked.string('')
    ),
    dropMetaData = cms.untracked.string('ALL'),
    eventAutoFlushCompressedSize = cms.untracked.int32(15728640),
    fastCloning = cms.untracked.bool(False),
    fileName = cms.untracked.string('file:HIG-RunIISpring16MiniAODv2-01205.root'),
    outputCommands = process.MINIAODSIMEventContent.outputCommands,
    overrideInputFileSplitLevels = cms.untracked.bool(True)
)

# Additional output definition

# Other statements
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '80X_mcRun2_asymptotic_v14', '')

# Path and EndPath definitions
process.Flag_trackingFailureFilter = cms.Path(process.goodVertices+process.trackingFailureFilter)
process.Flag_goodVertices = cms.Path(process.primaryVertexFilter)
process.Flag_CSCTightHaloFilter = cms.Path(process.CSCTightHaloFilter)
process.Flag_trkPOGFilters = cms.Path(process.trkPOGFilters)
process.Flag_trkPOG_logErrorTooManyClusters = cms.Path(~process.logErrorTooManyClusters)
process.Flag_EcalDeadCellTriggerPrimitiveFilter = cms.Path(process.EcalDeadCellTriggerPrimitiveFilter)
process.Flag_ecalLaserCorrFilter = cms.Path(process.ecalLaserCorrFilter)
process.Flag_globalSuperTightHalo2016Filter = cms.Path(process.globalSuperTightHalo2016Filter)
process.Flag_eeBadScFilter = cms.Path(process.eeBadScFilter)
process.Flag_METFilters = cms.Path(process.metFilters)
process.Flag_chargedHadronTrackResolutionFilter = cms.Path(process.chargedHadronTrackResolutionFilter)
process.Flag_globalTightHalo2016Filter = cms.Path(process.globalTightHalo2016Filter)
process.Flag_CSCTightHaloTrkMuUnvetoFilter = cms.Path(process.CSCTightHaloTrkMuUnvetoFilter)
process.Flag_HBHENoiseIsoFilter = cms.Path(process.HBHENoiseFilterResultProducer+process.HBHENoiseIsoFilter)
process.Flag_hcalLaserEventFilter = cms.Path(process.hcalLaserEventFilter)
process.Flag_HBHENoiseFilter = cms.Path(process.HBHENoiseFilterResultProducer+process.HBHENoiseFilter)
process.Flag_trkPOG_toomanystripclus53X = cms.Path(~process.toomanystripclus53X)
process.Flag_EcalDeadCellBoundaryEnergyFilter = cms.Path(process.EcalDeadCellBoundaryEnergyFilter)
process.Flag_trkPOG_manystripclus53X = cms.Path(~process.manystripclus53X)
process.Flag_HcalStripHaloFilter = cms.Path(process.HcalStripHaloFilter)
process.Flag_muonBadTrackFilter = cms.Path(process.muonBadTrackFilter)
process.Flag_CSCTightHalo2015Filter = cms.Path(process.CSCTightHalo2015Filter)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.MINIAODSIMoutput_step = cms.EndPath(process.MINIAODSIMoutput)

# Schedule definition
process.schedule = cms.Schedule(process.Flag_HBHENoiseFilter,process.Flag_HBHENoiseIsoFilter,process.Flag_CSCTightHaloFilter,process.Flag_CSCTightHaloTrkMuUnvetoFilter,process.Flag_CSCTightHalo2015Filter,process.Flag_globalTightHalo2016Filter,process.Flag_globalSuperTightHalo2016Filter,process.Flag_HcalStripHaloFilter,process.Flag_hcalLaserEventFilter,process.Flag_EcalDeadCellTriggerPrimitiveFilter,process.Flag_EcalDeadCellBoundaryEnergyFilter,process.Flag_goodVertices,process.Flag_eeBadScFilter,process.Flag_ecalLaserCorrFilter,process.Flag_trkPOGFilters,process.Flag_chargedHadronTrackResolutionFilter,process.Flag_muonBadTrackFilter,process.Flag_trkPOG_manystripclus53X,process.Flag_trkPOG_toomanystripclus53X,process.Flag_trkPOG_logErrorTooManyClusters,process.Flag_METFilters,process.endjob_step,process.MINIAODSIMoutput_step)

#do not add changes to your config after this point (unless you know what you are doing)
from FWCore.ParameterSet.Utilities import convertToUnscheduled
process=convertToUnscheduled(process)
process.load('Configuration.StandardSequences.PATMC_cff')
from FWCore.ParameterSet.Utilities import cleanUnscheduled
process=cleanUnscheduled(process)

# customisation of the process.

# Automatic addition of the customisation function from PhysicsTools.PatAlgos.slimming.miniAOD_tools
from PhysicsTools.PatAlgos.slimming.miniAOD_tools import miniAOD_customizeAllMC 

#call to customisation function miniAOD_customizeAllMC imported from PhysicsTools.PatAlgos.slimming.miniAOD_tools
process = miniAOD_customizeAllMC(process)

# End of customisation functions
