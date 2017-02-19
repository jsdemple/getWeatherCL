# ASCII weather art to be displayed in output

overcast = ''
snow = ''

cloudy = """

                      .

                      |
             .               /
              \       I
                          /
                \  ,g88R_
                  d888(`  ).                   _
         -  --==  888(     ).=--           .+(`  )`.
        )         Y8P(       '`.          :(   .    )
                .+(`(      .   )     .--  `.  (    ) )
               ((    (..__.:'-'   .=(   )   ` _`  ) )
        `.     `(       ) )       (   .  )     (   )  ._
          )      ` __.:'   )     (   (   ))     `-'.:(`  )
        )  )  ( )       --'       `- __.'         :(      ))
        .-'  (_.'          .')                    `(    )  ))
                          (_  )                     ` __.:'

        --..,___.--,--'`,---..-.--+--.,,-,,..._.--..-._.-a:f--.
        """

sunny = """
      ;   :   ;
   .   \_,!,_/   ,
    `.,'     `.,'
     /         \\
~ -- :         : -- ~
     \         /
    ,'`._   _.'`.
   '   / `!` \   `
      ;   :   ;  hjw
"""

rain = """
        ------               _____
       /      \ ___\     ___/    ___
    --/-  ___  /    \/  /  /    /   \\
   /     /           \__     //_     \\
  /                     \   / ___     |
  |           ___       \/+--/        /
   \__           \       \           /
      \__                 |          /
     \     /____      /  /       |   /
      _____/         ___       \/  /\\
           \__      /      /    |    |
         /    \____/   \       /   //
     // / / // / /\    /-_-/\//-__-
      /  /  // /   \__// / / /  //
     //   / /   //   /  // / // /
      /// // / /   /  //  / //
   //   //       //  /  // / /
     / / / / /     /  /    /
  ///  / / /  //  // /  // //
     ///    /    /    / / / /
///  /    // / /  // / / /  /
   // ///   /      /// / /
"""


class AsciiWeatherArt(object):
    def __init__(self, weather_condition):
        self.weather_condition = weather_condition


    def getArt(self, weather_condition):
        weather_condition = weather_condition.lower()
        print (weather_condition)
        if 'cloud' in weather_condition:
            return cloudy
        elif 'rain' or 'shower' in weather_condition:
            return rain
        elif 'sun' in weather_condition:
            return sunny
