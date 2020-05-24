# ======================western food store=============================               #WEN XIU
western_food = {'A': 'chicken cutlet: $5.50',
                'B': 'beef bolognese: $4.50',
                'C': 'cheese fries: $2.50',
                'D': 'fish and chips: $5.00',
                'E': 'chicken burger: $4.50',
                'F': 'fish burger: $4.80',
                'G': 'carbonara pasta: $4.50',
                'H': 'ham and egg sandwich: $3.00',
                'I': 'cheese omelette: $3.00',
                'J': 'egg tuna sandwich: $3.00'
                }

#western food offered everyday                                                       
western_food_days = {'Monday': [western_food['A'], western_food['D'], western_food['C'], western_food['G']],
                     'Tuesday': [western_food['A'], western_food['E'], western_food['F'], western_food['C']],
                     'Wednesday': [western_food['B'], western_food['C'], western_food['G'], western_food['D']],
                     'Thursday': [western_food['A'], western_food['D'], western_food['E'], western_food['C']],
                     'Friday': [western_food['B'], western_food['E'], western_food['G'], western_food['D']],
                     'Saturday': [western_food['A'], western_food['C'], western_food['E'], western_food['G']],
                     'Sunday': [western_food['B'], western_food['D'], western_food['F'], western_food['G']],
                     }

western_food_breakfast = {'Monday': [western_food['H'], western_food['J']],
                          'Tuesday': [western_food['I'], western_food['H']],
                          'Wednesday': [western_food['H'], western_food['J']],
                          'Thursday': [western_food['H'], western_food['J']],
                          'Friday': [western_food['I'], western_food ['H']],
                          'Saturday': [western_food['H'], western_food['I']],
                          'Sunday': [western_food['I'], western_food['J']]
                         }

# ======================korean food store=============================             #WEN XIU
korean_food = {'A': 'cheese ramyeon: $4.00',
               'B': 'bibimbap: $4.80',
               'C': 'hotplate chicken set: $5.00',
               'D': 'hotplate beef set: $5.50',
               'E': 'kimchi fried rice: $4.50',
               'F': 'kimchi soup: $4.00',
               'G': 'chicken ramyeon: $4.00',
               'H': 'korean pancake: $3.50',
               'I': 'tteokbokki: $3.50',
               'J': 'army stew: $4.00',
               }

#korean food offered everyday
korean_food_days = {'Monday': [korean_food['A'], korean_food['D'], korean_food['F'], korean_food['G']],
                     'Tuesday': [korean_food['B'], korean_food['E'], korean_food['G'], korean_food['C']],
                     'Wednesday': [korean_food['D'], korean_food['C'], korean_food['E'], korean_food['A']],
                     'Thursday': [korean_food['A'], korean_food['E'], korean_food['C'], korean_food['G']],
                     'Friday': [korean_food['B'], korean_food['C'], korean_food['F'], korean_food['D']],
                     'Saturday': [korean_food['A'], korean_food['C'], korean_food['D'], korean_food['F']],
                     'Sunday': [korean_food['B'], korean_food['D'], korean_food['G'], korean_food['C']]
                    }

korean_food_breakfast = {'Monday': [korean_food['I'], korean_food['H']],
                         'Tuesday': [korean_food['H'], korean_food['J']],
                         'Wednesday': [korean_food['I'], korean_food['H']],
                         'Thursday': [korean_food['H'], korean_food['J']],
                         'Friday': [korean_food['I'], korean_food['H']],
                         'Saturday': [korean_food['I'], korean_food['J']],
                         'Sunday': [korean_food['H'], korean_food['J']]
                        }


# ======================japanese food store=============================                  #WEN XIU
japanese_food = {'A': 'salmon rice: $4.50',
               'B': 'chicken teriyaki don: $4.00',
               'C': 'chicken udon: $3.80',
               'D': 'oyako don: $3.50',
               'E': 'tempura udon: $4.00',
               'F': 'teriyaki salmon don: $4.50 ',
               'G': 'chicken bento set: $4.50',
               'H': 'chawanmushi: $1.80',
               'I': 'miso soup: $1.50',
               'J': 'chicken udon: $3.80'
               }

#japanese food offered everyday
japanese_food_days = {'Monday': [japanese_food['A'], japanese_food['D'], japanese_food['F'], japanese_food['G']],
                      'Tuesday': [japanese_food['B'], japanese_food['E'], japanese_food['F'], japanese_food['D']],
                      'Wednesday': [japanese_food['D'], japanese_food['C'], japanese_food['G'], japanese_food['A']],
                      'Thursday': [japanese_food['A'], japanese_food['E'], japanese_food['C'], japanese_food['G']],
                      'Friday': [japanese_food['B'], japanese_food['C'], japanese_food['F'], japanese_food['D']],
                      'Saturday': [japanese_food['A'], japanese_food['C'], japanese_food['D'], japanese_food['G']],
                      'Sunday': [japanese_food['B'], japanese_food['D'], japanese_food['A'], japanese_food['G']]
                      }

japanese_food_breakfast = {'Monday': [japanese_food['I'], japanese_food ['H']],
                           'Tuesday': [japanese_food['J'], japanese_food ['H']],
                           'Wednesday': [japanese_food['I'], japanese_food ['H']],
                           'Thursday': [japanese_food['I'], japanese_food ['G']],
                           'Friday': [japanese_food['I'], japanese_food ['H']],
                           'Saturday': [japanese_food['I'], japanese_food ['J']],
                           'Sunday': [japanese_food['H'], japanese_food ['J']]
                           }

# ======================macdonalds store=============================                      #WEN XIU
macdonalds = {'A': 'mcchicken: $2',
              'B': 'mcspicy: $4.50',
              'C': 'fish ofillet: $2.50',
              'D': 'cheeseburger: $2.20',
              'E': 'chicken mcnuggets (6 pcs): $3.50',
              'F': 'mcdouble: $3.50',
              'G': 'double mcspicy: $5.50',
              'H': 'big breakfast: $5.50',
              'I': 'egg mcmuffin: $3.00',
              'J': 'sausage wrap: $3.00',
              }

#macdonalds offered everyday
macdonalds_food_days = {'Monday': [macdonalds['A'], macdonalds['D'], macdonalds['F'], macdonalds['G']],
                     'Tuesday': [macdonalds['B'], macdonalds['E'], macdonalds['D'], macdonalds['G']],
                     'Wednesday': [macdonalds['D'], macdonalds['C'], macdonalds['A'], macdonalds['G']],
                     'Thursday': [macdonalds['A'], macdonalds['E'], macdonalds['F'], macdonalds['C']],
                     'Friday': [macdonalds['B'], macdonalds['C'], macdonalds['D'], macdonalds['G']],
                     'Saturday': [macdonalds['A'], macdonalds['C'], macdonalds['B'], macdonalds['G']],
                     'Sunday': [macdonalds['B'], macdonalds['D'], macdonalds['F'], macdonalds['C']]
                    }

macdonalds_breakfast = {'Monday': [macdonalds['I'], macdonalds['H']],
                         'Tuesday': [macdonalds['I'], macdonalds['J']],
                         'Wednesday': [macdonalds['J'], macdonalds['H']],
                         'Thursday': [macdonalds['J'], macdonalds['I']],
                         'Friday': [macdonalds['I'], macdonalds['H']],
                         'Saturday': [macdonalds['J'], macdonalds['H']],
                         'Sunday': [macdonalds['J'], macdonalds['I']]
                        }

# ======================kfc store=============================                           #WEN XIU
KFC_food = {'A': '2 pieces chicken meal: $6.80',
            'B': 'zinger burger meal: $6.60',
            'C': '2 pieces tenders: $5.00',
            'D': 'popcorn chicken snackers: $4.00',
            'E': 'curry rice bowl meal: $7.50',
            'F': '3 pieces chicken meal: $8.90',
            'G': 'shroom burger meal: $5.00',
            'H': 'twister: $3.90',
            'I': 'brekkie burger: $3.00',
            'J': 'original recipe porridge: $2.50'
           }

#kfc food offered everyday
KFC_food_days = {'Monday': [KFC_food['A'], KFC_food['D'], KFC_food['F'], KFC_food['G']],
                 'Tuesday': [KFC_food['B'], KFC_food['E'], KFC_food['D'], KFC_food['G']],
                 'Wednesday': [KFC_food['D'], KFC_food['C'], KFC_food['A'], KFC_food['G']],
                 'Thursday': [KFC_food['A'], KFC_food['E'], KFC_food['F'], KFC_food['G']],
                 'Friday': [KFC_food['B'], KFC_food['C'], KFC_food['D'], KFC_food['G']],
                 'Saturday': [KFC_food['A'], KFC_food['C'], KFC_food['F'], KFC_food['B']],
                 'Sunday': [KFC_food['B'], KFC_food['D'], KFC_food['A'], KFC_food['G']]
                }

KFC_food_breakfast = {'Monday': [KFC_food['I'], KFC_food['J']],
                      'Tuesday': [KFC_food['H'], KFC_food['J']],
                      'Wednesday': [KFC_food['I'], KFC_food['H']],
                      'Thursday': [KFC_food['I'], KFC_food['J']],
                      'Friday': [KFC_food['J'], KFC_food['H']],
                      'Saturday': [KFC_food['I'], KFC_food['H']],
                      'Sunday': [KFC_food['I'], KFC_food['J']],
                     }


