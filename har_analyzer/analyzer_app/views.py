from django.shortcuts import render
from .forms import HarAnalysisForm
from .har_analyzer import analyze_har

def analyze_har_view(request):
    if request.method == 'POST':
        form = HarAnalysisForm(request.POST, request.FILES)
        if form.is_valid():
            har_file = form.save()
            analysis = analyze_har(har_file.har_file.path)
            return render(request, 'results.html', {'analysis': analysis})
    else:
        form = HarAnalysisForm()
    
    return render(request, 'upload.html', {'form': form})