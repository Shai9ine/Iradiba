from django.shortcuts import render

def main_page(request):
  return render(request, 'pages/main_page.html')
