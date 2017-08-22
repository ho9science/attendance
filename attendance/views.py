import gspread
from django.shortcuts import render
from oauth2client.service_account import ServiceAccountCredentials


def home(request):
	return render(request, 'info/home.html')

def analysis(request):
    return render(request, 'info/analysis.html')

def post_list(request):
    scope = ['https://spreadsheets.google.com/feeds']
    credentials = ServiceAccountCredentials.from_json_keyfile_name('mykey.json', scope)
    gc = gspread.authorize(credentials)

    wks = gc.open("11기_출석관리").sheet1
    val = wks.acell('B2').value

    return render(request, 'googleSheet/post_list.html', {'example':val})