# ASCII weather art to be displayed in output
# overcast source: 'http://www.ascii-code.com/ascii-art/nature/rains.php'
overcast = """
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
                        \__      /      /\__ |___/
                          \____/   \__ /
                """
# snow source: 'http://www.ascii-code.com/ascii-art/nature/snows.php'
snow = """
                     *  .  *
                   . _\/ \/_ .
                    \  \ /  /             .      .
      ..    ..    -==>: X :<==-           _\/  \/_
      '\    /'      / _/ \_ \              _\/\/_
        \\//       '  /\ /\  '         _\_\_\/\/_/_/_
   _.__\\\///__._    *  '  *            / /_/\/\_\ \
    '  ///\\\  '                           _/\/\_
        //\\                               /\  /\
      ./    \.             ._    _.       '      '
      ''    ''             (_)  (_)                  <> \  / <>
                            .\::/.                   \_\/  \/_/
           .:.          _.=._\\//_.=._                  \\//
      ..   \o/   ..      '=' //\\ '='             _<>_\_\<>/_/_<>_
      :o|   |   |o:         '/::\'                 <> / /<>\ \ <>
       ~ '. ' .' ~         (_)  (_)      _    _       _ //\\ _
           >O<             '      '     /_/  \_\     / /\  /\ \
       _ .' . '. _                        \\//       <> /  \ <>
      :o|   |   |o:                   /\_\\><//_/\
      ''   /o\   ''     '.|  |.'      \/ //><\\ \/
           ':'        . ~~\  /~~ .       _//\\_
jgs                   _\_._\/_._/_      \_\  /_/
                       / ' /\ ' \                   \o/
       o              ' __/  \__ '              _o/.:|:.\o_
  o    :    o         ' .'|  |'.                  .\:|:/.
    '.\'/.'                 .                 -=>>::>o<::<<=-
    :->@<-:                 :                   _ '/:|:\' _
    .'/.\'.           '.___/*\___.'              o\':|:'/o
  o    :    o           \* \ / */                   /o\
       o                 >--X--<
                        /*_/ \_*\
                      .'   \*/   '.
                            :
                            '"""

# partly_cloudy source: 'http://www.ascii-code.com/ascii-art/nature/clouds.php'
partly_cloudy = """

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
# cloudy source: 'http://www.ascii-code.com/ascii-art/nature/clouds.php'
cloudy = """
                        _
                      (`  ).                   _
                     (     ).              .:(`  )`.
        )           _(       '`.          :(   .    )
                .=(`(      .   )     .--  `.  (    ) )
               ((    (..__.:'-'   .+(   )   ` _`  ) )
        `.     `(       ) )       (   .  )     (   )  ._
          )      ` __.:'   )     (   (   ))     `-'.-(`  )
        )  )  ( )       --'       `- __.'         :(      ))
        .-'  (_.'          .')                    `(    )  ))
                          (_  )                     ` __.:'

        --..,___.--,--'`,---..-.--+--.,,-,,..._.--..-._.-a:f--.     """
# sunny source: 'http://www.ascii-code.com/ascii-art/nature/sun.php'
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
# rain source: 'http://www.ascii-code.com/ascii-art/nature/rains.php'
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
        if 'partly cloudy' in weather_condition:
            return partly_cloudy
        if 'cloud' in weather_condition:
            return cloudy
        elif 'rain' or 'shower' in weather_condition:
            return rain
        elif 'sun' in weather_condition:
            return sunny
        elif 'overcast' in weather_condition:
            return overcast
        elif 'snow' in weather_condition:
            return snow

