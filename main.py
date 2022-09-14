#import json
import speedtest

print("Loading servers...")
test = speedtest.Speedtest()

test.get_servers()
print("Choosing best server...")

best = test.get_best_server()

#print(json.dumps(best, indent=2))

print(f"\n{best['sponsor']} - {best['host']}")
print(f"{best['name']} - {best['country']}")

print("\n\nPerforming download test... \n")
print("Performing upload test... \n")

download_result = test.download()
upload_result = test.upload()

print(f"\nDownload speed: {download_result / 1024 / 1024:.2f} Mbits/s")
print(f"\nUpload speed: {upload_result / 1024 / 1024:.2f} Mbits/s")

ping_result = test.results.ping

print("\n===========================>")
print(f":                      {ping_result:.2f} ms")

print("\n\n end.")
