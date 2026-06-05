#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import pandas as pd
from pathlib import Path

def parse_vehicles_json(json_file):
    """Парсит JSON файл с данными о марках и моделях"""
    
    print(f"Чтение файла: {json_file}")
    
    try:
        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        print("JSON успешно загружен!")
        
        # Получаем данные по маркам и моделям
        vehicles = data.get('VehicleMarksModels', {})
        
        if not vehicles:
            print("Нет данных в VehicleMarksModels")
            return
        
        print(f"Найдено марок: {len(vehicles)}")
        
        # Создаем список для Excel
        rows = []
        total_models = 0
        
        for brand, brand_data in vehicles.items():
            brand_code = brand_data.get('code', '')
            brand_new = brand_data.get('new', False)
            
            models = brand_data.get('models', {})
            total_models += len(models)
            
            print(f"  Марка: {brand} - {len(models)} моделей")
            
            for model_name, model_data in models.items():
                rows.append({
                    'Марка': brand,
                    'Код марки': brand_code,
                    'Модель': model_name,
                    'Код модели': model_data.get('code', ''),
                    'Категория': model_data.get('category', ''),
                    'Иностранный': model_data.get('foreign', False),
                    'New': model_data.get('new', False),
                    'Prolongation': model_data.get('prolongation', False),
                    'Transition': model_data.get('transition', False)
                })
        
        print(f"\nВсего моделей: {total_models}")
        
        # Создаем DataFrame и сохраняем в Excel
        if rows:
            df = pd.DataFrame(rows)
            
            # Сохраняем в Excel
            output_file = 'vehicle_marks_models.xlsx'
            df.to_excel(output_file, index=False, engine='openpyxl')
            print(f"✅ Данные сохранены в {output_file}")
            
            # Показываем первые 5 строк
            print("\nПервые 5 записей:")
            print(df.head())
        else:
            print("❌ Нет данных для сохранения")
            
    except FileNotFoundError:
        print(f"❌ Файл {json_file} не найден")
        print("Проверьте, что файл существует в текущей директории")
        
    except json.JSONDecodeError as e:
        print(f"❌ Ошибка в JSON файле: {e}")
        print(f"Позиция ошибки: {e.pos}")
        
    except Exception as e:
        print(f"❌ Неожиданная ошибка: {e}")

if __name__ == "__main__":
    # Указываем имя JSON файла
    json_filename = "data.json"
    parse_vehicles_json(json_filename)
