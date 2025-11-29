from imagekitio import ImageKit

ik = ImageKit(
    public_key="PASTE_PUBLIC",
    private_key="PASTE_PRIVATE",
    url_endpoint="PASTE_ENDPOINT"
)

print(ik.list_files())
