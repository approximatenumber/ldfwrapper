# LDF File Wrapper - simple library that is wrapped around `ldfparser`

The main idea is to manipulate signals and frames of LDF file.

```
In [1]: from ldfwrapper import LDFWrapper                                                                                                                                  

In [2]: ldf = LDFWrapper('/home/user/ldf/Myfile.ldf')                                          

In [3]: ldf.frames                                                                                                                                                         
Out[3]: 
[{'name': 'Driver_side_buttons',
  'frame_id': 21,
  'publisher': 'LSPAS',
  'length': 4,
  'signals': [{'signal': 'Driver_window', 'offset': 0},
   {'signal': 'Passenger_window', 'offset': 4},
   {'signal': 'Door_look', 'offset': 8}]},
 {'name': 'IG',
  'frame_id': 16,
  'publisher': 'APA',
  'length': 3,
  'signals': [{'signal': 'Key_pos', 'offset': 0},
   {'signal': 'Door_lamp_R', 'offset': 4},
   {'signal': 'Door_Lamp_L', 'offset': 8}]}]

In [4]: ldf.signals                 
Out[4]: 
[{'name': 'APA1_ConfigSensorNum',
  'width': 4,
  'init_value': 0,
  'publisher': 'APA',
  'subscribers': [],
  'values': None},
 {'name': 'APA1_ConfigPASType',
  'width': 2,
  'init_value': 0,
  'publisher': 'APA',
  'subscribers': [],
  'values': None}]

In [5]: ldf.get_frame_by_id(21)                                                                                                                                            
Out[5]: 
{'name': 'Driver_side_buttons',
 'frame_id': 21,
 'publisher': 'LSPAS',
 'length': 4,
 'signals': [{'signal': 'Driver_window', 'offset': 0},
  {'signal': 'Passenger_window', 'offset': 4},
  {'signal': 'Door_look', 'offset': 8}]}

In [6]: ldf.get_frame_by_name('Pass_side_buttons')                                                                                                                         
Out[6]: 
{'name': 'Pass_side_buttons',
 'frame_id': 23,
 'publisher': 'RSPAS',
 'length': 3,
 'signals': [{'signal': 'Pass_side_commands_NewSignal', 'offset': 0}]}

In [7]: ldf.get_signal_by_name('Pass_side_commands_NewSignal')                                                                                                             
Out[7]: 
{'name': 'Pass_side_commands_NewSignal',
 'width': 4,
 'init_value': 0,
 'publisher': 'RSPAS',
 'subscribers': ['APA'],
 'values': None}

 ```