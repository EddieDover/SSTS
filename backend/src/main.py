import sys

import uvicorn

def start() -> None:
    uvicorn.run(
        "infrastructure.bootstrap:bootstrap", host="0.0.0.0", port=8000, reload=sys.argv[1]=="dev"
    )

if __name__ == "__main__":
    start()