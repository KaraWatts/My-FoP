import json

class SatData:

    def __init__(self, data_file):

        with open('sat.json', 'r') as infile:
            self._data = json.load(infile)

    def save_as_csv(self, dbn_list):
        header_list = self._data['meta']['view']['columns']
        headers =''
        for index in range(8, 13):
            headers = headers + header_list[index]['name'] + ','
        with open('output.csv', 'w') as outfile:
            outfile.write(headers + ('\n'))
            for school in self._data['data']:
                for dbn in dbn_list:
                    if dbn == school[8]:
                            for index in range(8, 13):
                                if school[index]:
                                    outfile.write(school[index] + ',')
                                    outfile.write(',')
                                else:
                            outfile.write('\n')
        
        


sd = SatData('sat.json')
dbns = ["02M303", "02M294", "01M450", "02M445"]
sd.save_as_csv(dbns)