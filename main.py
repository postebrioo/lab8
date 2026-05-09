import requests

def get_quote():
    url = "https://api.adviceslip.com/advice"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        
        data = response.json()
        
        # У цьому API порада лежить в об'єкті 'slip' під ключем 'advice'
        advice = data['slip']['advice']
        
        print(f"\nЦитата: {advice}")
        print(f"Автор: Advice Slip API")
        
    except Exception as e:
        print(f"На жаль, сервер не відповів. Спробуйте ще раз через хвилину або перевірте інтернет. Помилка: {e}")

if __name__ == "__main__":
    get_quote()
