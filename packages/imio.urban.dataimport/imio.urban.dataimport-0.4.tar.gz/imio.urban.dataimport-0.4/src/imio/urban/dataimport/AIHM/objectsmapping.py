# -*- coding: utf-8 -*-

from imio.urban.dataimport.AIHM.mappers import LicenceFactory, PortalTypeMapper, \
    IdMapper, ReferenceMapper, WorklocationMapper, PcaMapper, ParcellingsMapper, \
    ParcellingRemarksMapper, ObservationsMapper, ArchitectMapper, GeometricianMapper, \
    NotaryMapper, CompletionStateMapper, ContactFactory, ContactTitleMapper, \
    ContactNameMapper, ContactFirstnameMapper, ContactSreetMapper, ContactNumberMapper, \
    ContactZipcodeMapper, ContactCityMapper, ContactCountryMapper, ContactPhoneMapper, \
    ContactRepresentedByMapper, ContactIdMapper, ParcelFactory, ParcelDataMapper, \
    RadicalMapper, ExposantMapper, BisMapper, UrbanEventFactory, DepositEventTypeMapper, \
    DepositDateMapper, CompleteFolderEventTypeMapper, CompleteFolderDateMapper, \
    DecisionEventTypeMapper, DecisionDateMapper, NotificationDateMapper, DecisionMapper, \
    ErrorsMapper

from imio.urban.dataimport.access.mapper import AccessSimpleMapper as SimpleMapper

OBJECTS_NESTING = [
    (
        'LICENCE', [
            ('CONTACT', []),
            ('PARCEL', []),
            ('DEPOSIT EVENT', []),
            ('COMPLETE FOLDER EVENT', []),
            ('DECISION EVENT', []),
        ],
    ),
]

FIELDS_MAPPINGS = {
    'LICENCE':
    {
        'factory': [LicenceFactory],

        'mappers': {
            SimpleMapper: (
                {
                    'from': 'Travaux',
                    'to': 'licenceSubject',
                },
                {
                    'from': 'NumLot',
                    'to': 'subdivisionDetails',
                },
            ),

            IdMapper: {
                'from': ('CLEF',),
                'to': ('id',)
            },

            PortalTypeMapper: {
                'from': ('TYPE',),
                'to': ('portal_type', 'folderCategory',)
            },

            ReferenceMapper: {
                'from': ('CLEF'),
                'to': ('reference',)
            },

            WorklocationMapper: {
                'from': ('AdresseDuBien', 'NumPolParcelle', 'AncCommune'),
                'to': ('workLocations',)
            },

            PcaMapper: {
                'from': ('DatePPA',),
                'to': ('isInPCA', 'pca',),
            },

            ParcellingsMapper: {
                'from': ('AncCommune', 'NumLot', 'DateLot', 'DateLotUrbanisme'),
                'to': ('isInSubdivision', 'parcellings',),
            },

            ParcellingRemarksMapper: {
                'from': ('PPAObservations',),
                'to': ('locationTechnicalRemarks',),
            },

            ObservationsMapper: {
                'from': ('Observations',),
                'to': ('description',),
            },

            ArchitectMapper: {
                'allowed_containers': ['BuildLicence'],
                'from': ('NomArchitecte',),
                'to': ('architects',)
            },

            GeometricianMapper: {
                'allowed_containers': ['ParcelOutLicence'],
                'from': ('Titre', 'Nom', 'Prenom'),
                'to': ('geometricians',)
            },

            NotaryMapper: {
                'allowed_containers': ['UrbanCertificateOne', 'UrbanCertificateTwo', 'NotaryLetter'],
                'from': ('Titre', 'Nom', 'Prenom'),
                'to': ('notaryContact',),
            },

            CompletionStateMapper: {
                'from': ('DossierIncomplet', 'Refus'),
                'to': (),  # <- no field to fill, its the workflow state that has to be changed
            },

            ErrorsMapper: {
                'from': (),
                'to': ('description',),  # log all the errors in the description field
            }
        },
    },

    'CONTACT':
    {
        'factory': [ContactFactory],

        'mappers': {

            ContactTitleMapper: {
                'from': ('Titre', 'MandantTitre', 'MandantNom'),
                'to': 'personTitle',
            },

            ContactNameMapper: {
                'from': ('Nom', 'MandantNom'),
                'to': 'name1',
            },

            ContactFirstnameMapper: {
                'from': ('Prenom', 'MandantPrenom', 'MandantNom'),
                'to': 'name2',
            },

            ContactSreetMapper: {
                'from': ('Adresse', 'MandantAdresse', 'MandantNom'),
                'to': 'street',
            },

            ContactNumberMapper: {
                'from': ('NumPolice', 'BtePost', 'MandantNumPolice', 'MandantBtePost', 'MandantNom'),
                'to': 'number',
            },

            ContactZipcodeMapper: {
                'from': ('CP', 'MandantCP', 'MandantNom'),
                'to': 'zipcode',
            },

            ContactCityMapper: {
                'from': ('Localite', 'MandantLocalite', 'MandantNom'),
                'to': 'city',
            },

            ContactCountryMapper: {
                'from': ('Pays', 'MandantPays', 'MandantNom'),
                'to': 'Country',
            },

            ContactPhoneMapper: {
                'from': ('Telephone', 'MandantTelephone', 'MandantNom'),
                'to': 'phone',
            },

            ContactRepresentedByMapper: {
                'from': 'MandantNom',
                'to': 'representedBy',
            },

            ContactIdMapper: {
                'from': ('Nom', 'Prenom', 'MandantNom', 'MandantPrenom'),
                'to': 'id',
            },
        },
    },

    'PARCEL':
    {
        'factory': [ParcelFactory, {'portal_type': 'PortionOut'}],

        'mappers': {
            ParcelDataMapper: {
                'table': 'Parcelles',
                'KEYS': ('CLEF', 'CLEF'),
                'mappers': {
                    SimpleMapper:  (
                        {
                            'from': 'COMMUNE_ID',
                            'to': 'division',
                        },
                        {
                            'from': 'SECTION',
                            'to': 'section',
                        },
                    ),

                    RadicalMapper: {
                        'from': 'RADICAL',
                        'to': 'radical',
                    },
                    ExposantMapper: {
                        'from': 'EXPOSANT',
                        'to': ('exposant', 'puissance'),
                    },
                    BisMapper: {
                        'from': 'BIS',
                        'to': 'bis',
                    },
                },
            },
        },
    },

    'DEPOSIT EVENT':
    {
        'factory': [UrbanEventFactory],

        'mappers': {
            DepositEventTypeMapper: {
                'from': (),
                'to': 'eventtype',
            },

            DepositDateMapper: {
                'from': 'DateRecDem',
                'to': 'eventDate',
            }
        },
    },

    'COMPLETE FOLDER EVENT':
    {
        'factory': [UrbanEventFactory],

        'allowed_containers': ['BuildLicence', 'ParcelOutLicence'],

        'mappers': {
            CompleteFolderEventTypeMapper: {
                'from': (),
                'to': 'eventtype',
            },

            CompleteFolderDateMapper: {
                'from': 'AvisDossierComplet',
                'to': 'eventDate',
            },
        },
    },

    'DECISION EVENT':
    {
        'factory': [UrbanEventFactory],

        'mappers': {
            DecisionEventTypeMapper: {
                'from': 'Refus',
                'to': 'eventtype',
            },

            DecisionDateMapper: {
                'from': 'DateDecisionCollege',
                'to': 'decisionDate',
            },

            NotificationDateMapper: {
                'from': 'DateNotif',
                'to': 'eventDate',
            },

            DecisionMapper: {
                'from': 'Refus',
                'to': 'decision',
            },
        },
    },
}
