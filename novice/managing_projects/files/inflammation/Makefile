analyze:
	for i in data/*/*.dat; do python src/analyze_inflammation.py i; done;

clean:
	rm results/*.pdf

all: clean, analyze
