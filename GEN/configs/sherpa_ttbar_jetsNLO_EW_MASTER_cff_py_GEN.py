# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: Configuration/GenProduction/python/sherpa_ttbar_jetsNLO_EW_MASTER_cff.py --fileout file:sherpa_ttbar_jetsNLO_EW.root --mc --eventcontent RAWSIM --datatier GEN --conditions 106X_mc2017_realistic_v6 --beamspot Realistic25ns13TeVEarly2017Collision --step GEN --geometry DB:Extended --era Run2_2017 --no_exec
import FWCore.ParameterSet.Config as cms

from Configuration.Eras.Era_Run2_2017_cff import Run2_2017

process = cms.Process('GEN',Run2_2017)

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.Generator_cff')
process.load('IOMC.EventVertexGenerators.VtxSmearedRealistic25ns13TeVEarly2017Collision_cfi')
process.load('GeneratorInterface.Core.genFilterSummary_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(1)
)

# Input source
process.source = cms.Source("EmptySource")

process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('Configuration/GenProduction/python/sherpa_ttbar_jetsNLO_EW_MASTER_cff.py nevts:1'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition

process.RAWSIMoutput = cms.OutputModule("PoolOutputModule",
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('generation_step')
    ),
    compressionAlgorithm = cms.untracked.string('LZMA'),
    compressionLevel = cms.untracked.int32(1),
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('GEN'),
        filterName = cms.untracked.string('')
    ),
    eventAutoFlushCompressedSize = cms.untracked.int32(20971520),
    fileName = cms.untracked.string('file:sherpa_ttbar_jetsNLO_EW.root'),
    outputCommands = process.RAWSIMEventContent.outputCommands,
    splitLevel = cms.untracked.int32(0)
)

# Additional output definition

# Other statements
process.genstepfilter.triggerConditions=cms.vstring("generation_step")
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '106X_mc2017_realistic_v6', '')

process.generator = cms.EDFilter("SherpaGeneratorFilter",
    FetchSherpack = cms.bool(True),
    SherpaDefaultWeight = cms.double(1.0),
    SherpaParameters = cms.PSet(
        MPI_Cross_Sections = cms.vstring(
            ' MPIs in Sherpa, Model = Amisic:', 
            ' semihard xsec = 41.8409 mb,', 
            ' non-diffractive xsec = 17.0318 mb with nd factor = 0.3142.'
        ),
        Run = cms.vstring(
            ' (run){', 
            ' EVENTS 10; ERROR 0.99;', 
            ' FSF:=1.; RSF:=1.; QSF:=1.;', 
            ' SCALES STRICT_METS{FSF*MU_F2}{RSF*MU_R2}{QSF*MU_Q2};', 
            ' CORE_SCALE TTBar;', 
            ' EXCLUSIVE_CLUSTER_MODE 1;', 
            ' METS_BBAR_MODE=5', 
            ' NLO_CSS_PSMODE=1', 
            ' HEPMC_USE_NAMED_WEIGHTS 1;', 
            ' SCALE_VARIATIONS 0.25,0.25 0.25,1. 1.,0.25 1.,4. 4.,1. 4.,4.;', 
            ' PDF_LIBRARY LHAPDFSherpa;', 
            ' PDF_SET NNPDF30_nlo_as_0118;', 
            ' BEAM_1 2212; BEAM_ENERGY_1 = 6500.;', 
            ' BEAM_2 2212; BEAM_ENERGY_2 = 6500.;', 
            ' NJET:=4; LJET:=2,3; QCUT:=30.;', 
            ' ME_SIGNAL_GENERATOR Comix Amegic LOOPGEN;', 
            ' OL_PREFIX=/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/openloops/2.1.0-pafccj', 
            ' LOOPGEN:=OpenLoops;', 
            ' EVENT_GENERATION_MODE Unweighted;', 
            ' OL_PARAMETERS=ew_scheme 2 ew_renorm_scheme 1', 
            ' ASSOCIATED_CONTRIBUTIONS_VARIATIONS=EW EW|LO1 EW|LO1|LO2 EW|LO1|LO2|LO3;', 
            ' CSS_REWEIGHT=1', 
            ' REWEIGHT_SPLITTING_ALPHAS_SCALES 1', 
            ' REWEIGHT_SPLITTING_PDF_SCALES 1', 
            ' CSS_REWEIGHT_SCALE_CUTOFF=5.0', 
            ' HEPMC_INCLUDE_ME_ONLY_VARIATIONS=1', 
            ' INTEGRATION_ERROR=0.05;', 
            ' HARD_DECAYS On; HARD_SPIN_CORRELATIONS 1;', 
            ' HDH_STATUS[24,12,-11]=2', 
            ' HDH_STATUS[24,14,-13]=2', 
            ' HDH_STATUS[24,16,-15]=2', 
            ' HDH_STATUS[-24,-12,11]=2', 
            ' HDH_STATUS[-24,-14,13]=2', 
            ' HDH_STATUS[-24,-16,15]=2', 
            ' STABLE[24] 0; STABLE[6] 0; WIDTH[6] 0;', 
            '}(run)', 
            ' (processes){', 
            ' Process : 93 93 ->  6 -6 93{NJET};', 
            ' NLO_QCD_Mode 3 {LJET}; CKKW sqr(QCUT/E_CMS);', 
            ' ME_Generator Amegic {LJET};', 
            ' RS_ME_Generator Comix {LJET};', 
            ' Loop_Generator LOOPGEN;', 
            ' Associated_Contributions EW|LO1|LO2|LO3 {LJET};', 
            ' Order (*,0);', 
            ' Enhance_Observable VAR{log10(max(sqrt(H_T2)-PPerp(p[2])-PPerp(p[3]),(PPerp(p[2])+PPerp(p[3]))/2))}|2|3.3', 
            ' End process', 
            '}(processes)'
        ),
        parameterSets = cms.vstring(
            'MPI_Cross_Sections', 
            'Run'
        )
    ),
    SherpaPath = cms.string('./'),
    SherpaPathPiece = cms.string('./'),
    SherpaProcess = cms.string('ttbar_jetsNLO_EW'),
    SherpaResultDir = cms.string('Result'),
    SherpackChecksum = cms.string('01f56391ca09df4c615f37a9675e9da4'),
    SherpackLocation = cms.string('/cvmfs/cms.cern.ch/phys_generator/gridpacks/slc7_amd64_gcc700/13TeV/sherpa/2.2.8/'),
    crossSection = cms.untracked.double(-1),
    filterEfficiency = cms.untracked.double(1.0),
    maxEventsToPrint = cms.int32(0)
)


process.ProductionFilterSequence = cms.Sequence(process.generator)

# Path and EndPath definitions
process.generation_step = cms.Path(process.pgen)
process.genfiltersummary_step = cms.EndPath(process.genFilterSummary)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.RAWSIMoutput_step = cms.EndPath(process.RAWSIMoutput)

# Schedule definition
process.schedule = cms.Schedule(process.generation_step,process.genfiltersummary_step,process.endjob_step,process.RAWSIMoutput_step)
from PhysicsTools.PatAlgos.tools.helpers import associatePatAlgosToolsTask
associatePatAlgosToolsTask(process)
# filter all path with the production filter sequence
for path in process.paths:
	getattr(process,path).insert(0, process.ProductionFilterSequence)


# Customisation from command line

# Add early deletion of temporary data products to reduce peak memory need
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)
# End adding early deletion
