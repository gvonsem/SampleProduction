# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: step1 --filein dbs:/WprimeToWZToWhadZhad_narrow_M-3000_TuneCP5_13TeV-madgraph/RunIIFall17wmLHEGS-93X_mc2017_realistic_v3-v1/GEN-SIM --fileout file:B2G-RunIIFall17DRPremix-00059_step1.root --pileup_input dbs:/Neutrino_E-10_gun/RunIISummer17PrePremix-MC_v2_94X_mc2017_realistic_v9-v1/GEN-SIM-DIGI-RAW --mc --eventcontent PREMIXRAW --datatier GEN-SIM-RAW --conditions 94X_mc2017_realistic_v10 --step DIGIPREMIX_S2,DATAMIX,L1,DIGI2RAW,HLT:2e34v40 --nThreads 4 --datamix PreMix --era Run2_2017 --python_filename B2G-RunIIFall17DRPremix-00059_1_cfg.py --no_exec --customise Configuration/DataProcessing/Utils.addMonitoring -n 10
import FWCore.ParameterSet.Config as cms

from Configuration.StandardSequences.Eras import eras

process = cms.Process('HLT',eras.Run2_2017)

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.DigiDMPreMix_cff')
process.load('SimGeneral.MixingModule.digi_MixPreMix_cfi')
process.load('Configuration.StandardSequences.DataMixerPreMix_cff')
process.load('Configuration.StandardSequences.SimL1EmulatorDM_cff')
process.load('Configuration.StandardSequences.DigiToRawDM_cff')
process.load('HLTrigger.Configuration.HLT_2e34v40_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(10)
)

# Input source
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring('/store/group/cmst3/user/gvonsem/SampleProduction/Wprime_WZ_WhadZhad_Herwig7/Wprime_WZ_WhadZhad_narrow_M3000_herwig7_GEN-SIM/190726_110437/0000/Wprime_WZ_WhadZhad_narrow_M3000_herwig7_1.root'),
    secondaryFileNames = cms.untracked.vstring()
)

process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('step1 nevts:10'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition

process.PREMIXRAWoutput = cms.OutputModule("PoolOutputModule",
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('GEN-SIM-RAW'),
        filterName = cms.untracked.string('')
    ),
    fileName = cms.untracked.string('file:B2G-RunIIFall17DRPremix-00059_step1.root'),
    outputCommands = process.PREMIXRAWEventContent.outputCommands,
    splitLevel = cms.untracked.int32(0)
)

# Additional output definition

# Other statements
process.mix.digitizers = cms.PSet(process.theDigitizersMixPreMix)
process.mixData.input.fileNames = cms.untracked.vstring(['/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MCv2_correctPU_94X_mc2017_realistic_v9-v1/80021/F4CEFFB5-FC0E-E811-A015-0025905B857E.root', '/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MCv2_correctPU_94X_mc2017_realistic_v9-v1/80022/72092F18-080F-E811-9A77-0025905A610C.root', '/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MCv2_correctPU_94X_mc2017_realistic_v9-v1/80022/6639B410-110F-E811-8BD3-0CC47A4C8F10.root', '/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MCv2_correctPU_94X_mc2017_realistic_v9-v1/80022/B46B6480-110F-E811-A9A0-0CC47A7C3572.root', '/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MCv2_correctPU_94X_mc2017_realistic_v9-v1/80021/08F933F2-110F-E811-9723-0CC47A4D7606.root', '/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MCv2_correctPU_94X_mc2017_realistic_v9-v1/80021/1EB39C59-FE0E-E811-8724-0025905B8580.root', '/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MCv2_correctPU_94X_mc2017_realistic_v9-v1/80022/FEB40EDF-010F-E811-9C81-0025905B85B2.root', '/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MCv2_correctPU_94X_mc2017_realistic_v9-v1/80022/E6281466-0F0F-E811-B8F3-0CC47A4D7678.root', '/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MCv2_correctPU_94X_mc2017_realistic_v9-v1/80021/48661D80-100F-E811-B625-0CC47A7C360E.root', '/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MCv2_correctPU_94X_mc2017_realistic_v9-v1/80022/329AF42D-130F-E811-B39F-0CC47A4D76C8.root', '/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MCv2_correctPU_94X_mc2017_realistic_v9-v1/80022/FCB963F4-020F-E811-ACB6-0025905B85FC.root', '/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MCv2_correctPU_94X_mc2017_realistic_v9-v1/80022/547D9CA6-100F-E811-BB54-0CC47A4D76AC.root', '/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MCv2_correctPU_94X_mc2017_realistic_v9-v1/80022/0C97B915-120F-E811-B2D5-0CC47A4C8EBA.root', '/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MCv2_correctPU_94X_mc2017_realistic_v9-v1/80008/B4359217-190F-E811-B2A6-0CC47A4C8EBA.root', '/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MCv2_correctPU_94X_mc2017_realistic_v9-v1/80008/44FE4C44-010F-E811-9C92-0025905A4964.root', '/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MCv2_correctPU_94X_mc2017_realistic_v9-v1/80008/9E65897C-070F-E811-BD0D-0025905A6082.root', '/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MCv2_correctPU_94X_mc2017_realistic_v9-v1/80022/FEC48B25-010F-E811-8C4C-0025905B8610.root', '/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MCv2_correctPU_94X_mc2017_realistic_v9-v1/80022/5AA3F52E-120F-E811-AC43-0CC47A4D7664.root', '/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MCv2_correctPU_94X_mc2017_realistic_v9-v1/80008/E6B23D2F-100F-E811-8363-0CC47A4D765E.root', '/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MCv2_correctPU_94X_mc2017_realistic_v9-v1/80020/9E4BB692-100F-E811-9996-0CC47A7C360E.root', '/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MCv2_correctPU_94X_mc2017_realistic_v9-v1/80022/E65DB7A4-020F-E811-BE0A-0025905B85B2.root', '/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MCv2_correctPU_94X_mc2017_realistic_v9-v1/80009/FC089E03-2E0F-E811-AF7A-0CC47A4D7646.root', '/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MCv2_correctPU_94X_mc2017_realistic_v9-v1/80022/105DACB1-1D0F-E811-BBD3-0025905A60B0.root', '/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MCv2_correctPU_94X_mc2017_realistic_v9-v1/80023/3455DBB3-250F-E811-966A-0CC47A7C345E.root', '/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MCv2_correctPU_94X_mc2017_realistic_v9-v1/80009/8A186AB2-240F-E811-845E-0CC47A7C34A6.root', '/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MCv2_correctPU_94X_mc2017_realistic_v9-v1/80009/D22C2AEF-250F-E811-BE36-0CC47A4D75F2.root', '/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MCv2_correctPU_94X_mc2017_realistic_v9-v1/80023/E2F8A5CE-250F-E811-88F8-0CC47A4D7692.root', '/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MCv2_correctPU_94X_mc2017_realistic_v9-v1/80023/343ADEE3-260F-E811-B970-0CC47A7C3450.root', '/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MCv2_correctPU_94X_mc2017_realistic_v9-v1/80023/04F423B4-270F-E811-8C59-0CC47A7C345C.root', '/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MCv2_correctPU_94X_mc2017_realistic_v9-v1/80022/18A6B579-190F-E811-9F1C-0025905A6056.root', '/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MCv2_correctPU_94X_mc2017_realistic_v9-v1/80022/DE804646-1B0F-E811-9F9D-0025905B860E.root', '/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MCv2_correctPU_94X_mc2017_realistic_v9-v1/80022/68A08986-1B0F-E811-8EDC-0025905A6136.root'])
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '94X_mc2017_realistic_v10', '')

# Path and EndPath definitions
process.digitisation_step = cms.Path(process.pdigi)
process.datamixing_step = cms.Path(process.pdatamix)
process.L1simulation_step = cms.Path(process.SimL1Emulator)
process.digi2raw_step = cms.Path(process.DigiToRaw)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.PREMIXRAWoutput_step = cms.EndPath(process.PREMIXRAWoutput)

# Schedule definition
process.schedule = cms.Schedule(process.digitisation_step,process.datamixing_step,process.L1simulation_step,process.digi2raw_step)
process.schedule.extend(process.HLTSchedule)
process.schedule.extend([process.endjob_step,process.PREMIXRAWoutput_step])
from PhysicsTools.PatAlgos.tools.helpers import associatePatAlgosToolsTask
associatePatAlgosToolsTask(process)

#Setup FWK for multithreaded
process.options.numberOfThreads=cms.untracked.uint32(4)
process.options.numberOfStreams=cms.untracked.uint32(0)

# customisation of the process.

# Automatic addition of the customisation function from Configuration.DataProcessing.Utils
from Configuration.DataProcessing.Utils import addMonitoring 

#call to customisation function addMonitoring imported from Configuration.DataProcessing.Utils
process = addMonitoring(process)

# Automatic addition of the customisation function from HLTrigger.Configuration.customizeHLTforMC
from HLTrigger.Configuration.customizeHLTforMC import customizeHLTforMC 

#call to customisation function customizeHLTforMC imported from HLTrigger.Configuration.customizeHLTforMC
process = customizeHLTforMC(process)

# End of customisation functions

# Customisation from command line

# Add early deletion of temporary data products to reduce peak memory need
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)
# End adding early deletion






