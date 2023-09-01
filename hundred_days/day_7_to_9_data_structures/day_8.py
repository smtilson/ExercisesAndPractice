cars = {
    'Ford': ['Falcon', 'Focus', 'Festiva', 'Fairlane'],
    'Holden': ['Commodore', 'Captiva', 'Barina', 'Trailblazer'],
    'Nissan': ['Maxima', 'Pulsar', '350Z', 'Navara'],
    'Honda': ['Civic', 'Accord', 'Odyssey', 'Jazz'],
    'Jeep': ['Grand Cherokee', 'Cherokee', 'Trailhawk', 'Trackhawk']
}


def get_all_jeeps():
    base = ''
    for car in cars['Jeep']:
        base+=car+', '
    return base[:-2]


def get_first_model_each_manufacturer(cars=cars):
    models=[]
    for manufacturer in cars.keys():
        models.append(cars[manufacturer][0])
    return models

def get_all_matching_models(cars=cars, grep='trail'):
    models_special = []
    for models in cars.values():
        for model in models:
            if grep.lower() in model.lower():
                models_special.append(model)
    models_special.sort()
    return models_special


def sort_car_models(cars=cars):
    for manufacturer in cars.keys():
        cars[manufacturer].sort()
    return cars



def test_get_all_jeeps():
    expected = 'Grand Cherokee, Cherokee, Trailhawk, Trackhawk'
    actual = get_all_jeeps()
    assert type(actual) == str
    assert actual == expected


def test_get_first_model_each_manufacturer():
    actual = get_first_model_each_manufacturer()
    expected = ['Falcon', 'Commodore', 'Maxima', 'Civic', 'Grand Cherokee']
    assert actual == expected


def test_get_all_matching_models_default_grep():
    expected = ['Trailblazer', 'Trailhawk']
    assert get_all_matching_models() == expected


def test_get_all_matching_models_different_grep():
    expected = ['Accord', 'Commodore', 'Falcon']
    assert get_all_matching_models(grep='CO') == expected


def test_sort_dict_alphabetically():
    actual = sort_car_models()
    # Order of keys should not matter, two dicts are equal if they have the
    # same keys and the same values.
    # The car models (values) need to be sorted here though
    expected = {
        'Ford': ['Fairlane', 'Falcon', 'Festiva', 'Focus'],
        'Holden': ['Barina', 'Captiva', 'Commodore', 'Trailblazer'],
        'Honda': ['Accord', 'Civic', 'Jazz', 'Odyssey'],
        'Jeep': ['Cherokee', 'Grand Cherokee', 'Trackhawk', 'Trailhawk'],
        'Nissan': ['350Z', 'Maxima', 'Navara', 'Pulsar'],
    }
    assert actual == expected