import pandas as pd
import numpy as np
import os

'''
csv파일의 원하는 column 의 값을 가져와서 교집합, 합집합 알아보기!!

작동 순서
1. CSV 읽어서 DF 로 만들기
2. DF 의 Column (Series) 를 가져와 Numpy 로 만들기
3. Numpy 끼리 비교
4. 비교값 DF 로 만들기 (Column 명 : applicationNumber)
'''

class ResultValue:

    def __init__(self, file_paths: list, column_name: str):
        self.file_paths = file_paths
        self.column_name = column_name
        

    def get_df(self, file_name):
        self.df = pd.read_csv(file_name)
        return self.df

    def get_series(self):
        self.series = self.df[self.column_name]
        return self.series
    
    def change_array(self, series):
        return np.array(series)
        
    def get_intersection(self):
        self.result = np.intersect1d(self.np_first, self.np_second)
        print(f'Intersectection value : {len(self.result)} ')
        return self.result

    def get_difference(self):
        self.result = np.setdiff1d(self.np_first, self.np_second)
        print(f'Difference value : {len(self.result)} ')
        return self.result

    def create_result_df(self):
        self.result_df = pd.DataFrame(self.result)
        self.result_df.columns = ['applicationNumber']
        print("")
        print("")
        
        print(self.result_df)
        return self.result_df

    def main(self, method = None):
        
        np_list = []
        
        for file_name in self.file_paths:
            self.get_df(file_name)
            series = self.get_series()
            np_array = self.change_array(series)
            np_list.append(np_array)
    
        self.np_first, self.np_second = np_list[0], np_list[1]
    
        if method == 1:
            self.get_difference()

        elif method == 2:
            self.get_intersection()

        elif method == 3:
            self.get_intersection()    
            self.create_result_df()
            self.get_difference()
            
        self.create_result_df()
            

if __name__=='__main__':
    base_root = '/datacore/airflow_kipris/appnum'
    print('기본 경로 >> ', base_root)
    method = int(input('CHOOSE :: 1. Difference (차집합), 2.Intersection (교집합) 3. Both (둘 다)? : '))
    file_name = str(input('파일 1의 경로 : '))
    file_name2 = str(input('파일 2의 경로 : '))
    file_list = [os.path.join(base_root,file_name), os.path.join(base_root, file_name2)]

    result_value = ResultValue(file_list, 'applicationNumber')
    result_value.main(method)