from django.shortcuts import render

# Create your views here.
def menu(request):
    context = {"menu": """The menu page displays a list of available food and beverage items for customers. 
It helps users easily browse different categories such as coffee, tea, snacks, 
and desserts. Each item in the menu may include details like the name, price, 
and description of the product. The menu page is designed to make it simple 
for customers to choose their preferred items and place orders quickly."""}  
    return render(request, 'menu.html', context)

def about(request):
    context = {"info": """Details are specific pieces of information that add depth and context, while information is the broader set of facts or knowledge about a subject.
Difference Between Details and Information
Information refers to the overall body of facts, data, or knowledge about a topic. It provides the framework or context within which specific points can be understood. For example, information about a car accident might include general statistics on accidents, safety tips, or legal implications."""}
    return render(request, 'about.html', context)