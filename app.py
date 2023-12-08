# Standard lib's JSON library
import json

# Spin SDKs
from spin_http import Response
from spin_key_value import kv_open_default


# This just creates a simple page hit counter that is stored in a JSON entry
# inside of Spin's KV store.
def handle_request(request):
    # Open the default KV store
    # IMPORTANT: You need to enable default key value storage in spin.toml
    store = kv_open_default()

    # Get the page if it exists
    page_counter = json.loads(store.get("page_counter") or b"{}")

    if "count" in page_counter:
        # If we have already started a counter, increment it
        page_counter["count"] = page_counter["count"] + 1
    else:
        # Otherwise initialize it
        page_counter["count"] = 1

    # Serialize back to JSON and store it.
    save_data = bytes(json.dumps(page_counter), "utf-8")
    store.set("page_counter", save_data)

    # Send back the page count
    return Response(
        200,
        {"content-type": "text/plain"},
        bytes(f"Hello visitor {page_counter['count']}", "utf-8"),
    )
