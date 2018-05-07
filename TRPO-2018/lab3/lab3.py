import json
import statistics


def j_son():
    x_current_speed = 4
    temperature = 12
    salinity = 16
    csll = []
    templl = []
    salll = []
    
    j_file = 'E05_aanderaa_all_36a0_a9c1_9ca0.json'
    with open(j_file, 'r') as f:
        data = json.loads(f.read())
        for i in range(len(data['table']['rows'])):
            if data['table']['rows'][i][x_current_speed + 1] == 0:
                csll.append(data['table']['rows'][i][x_current_speed])
            if data['table']['rows'][i][temperature + 1] == 0:
                templl.append(data['table']['rows'][i][temperature])
            if data['table']['rows'][i][salinity + 1] == 0:
                salll.append(data['table']['rows'][i][salinity])
        
        min_cs = min(csll)
        max_cs = max(csll)
        mid_cs = statistics.mean(csll)
        
        min_t = min(templl)
        max_t = max(templl)
        mid_t = statistics.mean(templl)
        
        min_sal = min(salll)
        max_sal = max(salll)
        mid_sal = statistics.mean(salll)
        
        for i in range(len(data['table']['rows'])):
            if min_cs == data['table']['rows'][i][x_current_speed]:
                min_cs_time = data['table']['rows'][i][3]
            if max_cs == data['table']['rows'][i][x_current_speed]:
                max_cs_time = data['table']['rows'][i][3]
            if min_t == data['table']['rows'][i][temperature]:
                min_t_time = data['table']['rows'][i][3]
            if max_t == data['table']['rows'][i][temperature]:
                max_t_time = data['table']['rows'][i][3]
            if min_sal == data['table']['rows'][i][salinity]:
                min_s_time = data['table']['rows'][i][3]
            if max_sal == data['table']['rows'][i][salinity]:
                max_s_time = data['table']['rows'][i][3]
        
        print(json.dumps(['current_speed: ', {'start_date': data['table']['rows'][0][3][0:10],
                                              'end_date': data['table']['rows'][-1][3][0:10],
                                              'num_records': len(data['table']['rows']), 'min_current_speed': min_cs,
                                              'min_time': min_cs_time,
                                              'max_current_speed': max_cs, 'max_time': max_cs_time,
                                              'avg_current_speed': mid_cs},
                          'temperature: ', {'start_date': data['table']['rows'][0][3][0:10],
                                            'end_date': data['table']['rows'][-1][3][0:10],
                                            'num_records': len(data['table']['rows']), 'min_current_speed': min_t,
                                            'min_time': min_t_time,
                                            'max_current_speed': max_t, 'max_time': max_t_time,
                                            'avg_current_speed': mid_t},
                          'salinity: ', {'start_date': data['table']['rows'][0][3][0:10],
                                         'end_date': data['table']['rows'][-1][3][0:10],
                                         'num_records': len(data['table']['rows']), 'min_current_speed': min_sal,
                                         'min_time': min_s_time,
                                         'max_current_speed': max_sal, 'max_time': max_s_time,
                                         'avg_current_speed': mid_sal}], sort_keys=True, indent=4))


if __name__ == "__main__":
    j_son()
