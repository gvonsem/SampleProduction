import FWCore.ParameterSet.Config as cms

externalLHEProducer = cms.EDProducer("ExternalLHEProducer",
    args = cms.vstring('/cvmfs/cms.cern.ch/phys_generator/gridpacks/2017/13TeV/powheg/V2/TT_hvq/TT_hdamp_NNPDF31_NNLO_dilepton.tgz'),
    nEvents = cms.untracked.uint32(5000),
    numberOfParameters = cms.uint32(1),
    outputFile = cms.string('cmsgrid_final.lhe'),
    scriptName = cms.FileInPath('GeneratorInterface/LHEInterface/data/run_generic_tarball_cvmfs.sh')
)

#Link to datacards:
#https://github.com/jfernan2/genproductions/blob/54a8155135fb7f0d9cef82dbbbbdcdbb59ea55f0/bin/Powheg/production/2017/13TeV/TT_hvq/TT_hdamp_NNPDF31_NNLO_dilepton.input


import FWCore.ParameterSet.Config as cms
from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.MCTunes2017.PythiaCP5Settings_cfi import *
from Configuration.Generator.Pythia8PowhegEmissionVetoSettings_cfi import *
from Configuration.Generator.PSweightsPythia.PythiaPSweightsSettings_cfi import *
generator = cms.EDFilter("Pythia8HadronizerFilter",
maxEventsToPrint = cms.untracked.int32(1),
pythiaPylistVerbosity = cms.untracked.int32(1),
filterEfficiency = cms.untracked.double(1.0),
pythiaHepMCVerbosity = cms.untracked.bool(False),
comEnergy = cms.double(13000.),
PythiaParameters = cms.PSet(
pythia8CommonSettingsBlock,
pythia8CP5SettingsBlock,
pythia8PowhegEmissionVetoSettingsBlock,
pythia8PSweightsSettingsBlock,
processParameters = cms.vstring(
        'POWHEG:nFinal = 2', ## Number of final state particles
        ## (BEFORE THE DECAYS) in the LHE
        ## other than emitted extra parton
        'TimeShower:mMaxGamma = 1.0',#cutting off lepton-pair production
        ##in the electromagnetic shower
        ##to not overlap with ttZ/gamma* samples
        '6:m0 = 172.5',    # top mass'

        '24:onMode = off',
        '24:onIfAny = 11 13',

        '411:onMode = off',
        '411:onIfMatch = 321 211 211',
        '413:onMode = off',
        '413:onIfMatch = 421 211',
        '421:onMode = off',
        '421:onIfMatch = -321 211',
        '421:offIfAny = 321',
        '421:onIfMatch = 321 211',
        '431:onMode = off',
        '431:onIfMatch = 321 321 211',

        '511:onMode = off',
        '511:onIfMatch = 12 11 411',
        '511:onIfMatch = 12 11 413',
        '511:onIfMatch = 14 13 411',
        '511:onIfMatch = 14 13 413',

        '521:onMode = off',
        '521:onIfMatch = 12 11 421',
        '521:onIfMatch = 14 13 421',

        '531:onMode = off',
        '531:onIfMatch = 12 11 431',
        '531:onIfMatch = 14 13 431',

        '4122:onMode = off',
        '4122:onIfMatch = 2212 313',

        '5122:onMode = off',
        '5122:onIfMatch = 12 11 4122',
        '5122:onIfMatch = 14 13 4122'
        ),
parameterSets = cms.vstring('pythia8CommonSettings',
'pythia8CP5Settings',
'pythia8PowhegEmissionVetoSettings',
'pythia8PSweightsSettings',
'processParameters'
)
)
)
ProductionFilterSequence = cms.Sequence(generator)