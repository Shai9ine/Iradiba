from django.shortcuts import render
# hi
def main_page(request):
  return render(request, 'pages/main_page.html')
