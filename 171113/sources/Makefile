APPS=$(sort $(basename $(wildcard *.cpp)))

.PHONY: all clean

all: $(APPS)

%: %.cpp
	g++ $^ -o $@ -Wall -Wextra -Werror -Wno-unknown-pragmas -pthread

clean:
	rm $(APPS) >/dev/null 2>&1 || true
