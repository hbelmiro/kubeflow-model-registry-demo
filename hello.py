from model_registry import ModelRegistry

# The MinIO service in Kubernetes
MINIO_ENDPOINT = "http://minio-service.kubeflow.svc.cluster.local:9000"


def main():
    print("Initializing...")

    registry = ModelRegistry(
        server_address="http://model-registry-service.kubeflow.svc.cluster.local",  # The MR service in Kubernetes
        port=8080,
        author="hbelmiro",
        user_token="non-used",  # Just to avoid a warning
        is_secure=False
    )

    print("Registry created")

    registry.register_model(
        name="my-model",
        uri=MINIO_ENDPOINT + "/artifacts/get?source=minio&bucket=mlpipeline&key=v2%2Fartifacts%2Ffraud-detection-e2e-pipeline%2F698d78b3-862c-46e9-b563-306e4d29a233%2Ftrain-model%2Fd52ccd24-99cf-423e-a30a-689432cc2bf1%2Fmodel",
        version="2.0.0",
        description="lorem ipsum",
        model_format_name="onnx",
        model_format_version="1",
        storage_key="mlpipeline-minio-artifact",
        metadata={
            # can be one of the following types
            "int_key": 1,
            "bool_key": False,
            "float_key": 3.14,
            "str_key": "str_value",
        }
    )

    print("Model registered")

    model = registry.get_registered_model("my-model")
    print(model)


if __name__ == "__main__":
    main()
