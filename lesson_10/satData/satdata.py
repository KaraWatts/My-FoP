import json

class SatData:

    def __init__(self, data_file):

        with open('sat.json', 'r') as infile:
            self._data_all = json.load(infile)
        header_list = self._data_all['meta']['view']['columns']
        headers =''
        for index in range(8, 13):
            headers = headers + header_list[index]['name'] + ','
        formatted_data = {}
        for school in self._data_all['data']:
            formatted_row = ''  
            for index in range(8, 13):
                if school[index]:
                    formatted_row = formatted_row + school[index] + ','
                else:
                    formatted_row += ','
                formatted_data[school[8]] = formatted_row
        self._data = formatted_data
        self._header = headers


    def save_as_csv(self, dbn_list):
        with open('output.csv', 'w') as outfile:
            outfile.write(self._header + ('\n'))
            for dbn in dbn_list:
                if dbn in self._data:
                    outfile.write(self._data[dbn] + "\n") 
                    
            
        


sd = SatData('sat.json')
dbns = ["02M303", "02M294", "01M450", "02M445"]
sd.save_as_csv(dbns)