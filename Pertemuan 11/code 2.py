class Model(object):
    services = {
        'email': {'number': 1000, 'price': 2},
        'sms': {'number': 1000, 'price': 10},
        'voice': {'number': 1000, 'price': 15},
    }

class View(object):  # English
    def list_services(self, services):
        print("Services Provided:")
        for svc in services:
            print(svc)

    def list_pricing(self, services):
        print("Pricing for Services:")
        for svc in services:
            print("For", Model.services[svc]['number'],
                  svc, "message you pay $",
                  Model.services[svc]['price'])

class View2(object):  # Indonesian
    def list_services(self, services):
        print("Layanan yang disediakan:")
        for svc in services:
            print(svc)

    def list_pricing(self, services):
        print("Tarif tiap layanan:")
        for svc in services:
            print("Untuk setiap", Model.services[svc]['number'],
                  svc, "anda membayar $",
                  Model.services[svc]['price'])

class Controller(object):
    def __init__(self, view):
        self.model = Model()
        self.view = view

    def get_services(self):
        services = self.model.services.keys()
        return self.view.list_services(services)

    def get_pricing(self):
        services = self.model.services.keys()
        return self.view.list_pricing(services)

# Mapping bahasa ke view class
language_map = {
    '1': View(),
    '2': View2()
}

# Input dari user
lang = input("What language do you choose? [1]English [2]Indonesia: ")
view = language_map.get(lang)

# Tampilkan hasil jika valid, jika tidak error
if view:
    controller = Controller(view)
    controller.get_services()
    controller.get_pricing()
else:
    print("Error, choose the language number!")
    print("Error, choose the language number!")
