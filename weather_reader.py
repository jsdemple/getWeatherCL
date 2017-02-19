import urllib.request
import xml.etree.ElementTree as ET
import weather_ascii


def get_xml(xml_url):
    response = urllib.request.urlopen(xml_url)
    xml_data = response.read()
    # save to .xml
    filename = xml_url.split('/')[-1]
    with open(filename, 'wb') as writer:
        writer.write(xml_data)
    return filename


def parse_xml(xml_file, tags):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    # get data for each tag
    dataset = []
    for tag in tags:
        data_tuple = (tag, root.findall(tag[0])[0].text)
        dataset.append(data_tuple)
        if data_tuple[0][0] == 'weather':
            cur_cond = data_tuple[1]
    if cur_cond is None:
        return dataset
    else:
        return dataset, cur_cond


def get_ascii_art(current_conditions):
    art_obj = weather_ascii.AsciiWeatherArt(current_conditions)
    art_str = art_obj.getArt(current_conditions)
    return art_str


def present_weather(dataset_list, asciiart):
    if asciiart:
        print(asciiart)
    print('**********************CURRENT WEATHER REPORT**********************')
    for item in dataset_list:
        if len(item[0][1]) > 3:
            print(item[0][1], item[1])
        else:
            print(item[1])
    print('******************************************************************')


## MAIN CODE
SLCfeed = 'http://w1.weather.gov/xml/current_obs/KSLC.xml'
# weather_details = ['location', 'weather', 'temperature_string', 'windchill_string', 'relative_humidity', 'observation_time']
weather_details = [('location', 'Location:'),
                   ('weather', 'Currently:     '),
                   ('temperature_string', 'Temperature:   '),
                   ('windchill_string', 'Feels like:    '),
                   ('relative_humidity', 'Humidity:      '),
                   ('observation_time', '\n')]


# print (cloudy)
xml_filename = get_xml(SLCfeed)
weather_dataset, current_conditions = parse_xml(xml_filename, weather_details)
art = get_ascii_art(current_conditions)
# art = get_ascii_art('sun')

present_weather(weather_dataset, art)


## EXAMPLE OUTPUT
"""
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
        
**********************CURRENT WEATHER REPORT**********************
Location: Salt Lake City, Salt Lake City International Airport, UT
Currently:      Mostly Cloudy
Temperature:    49.0 F (9.4 C)
Feels like:     44 F (7 C)
Humidity:       59
Last Updated on Feb 18 2017, 10:54 pm MST
******************************************************************
"""

