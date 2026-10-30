from sklearn.datasets import fetch_lfw_people

def main():
    dataset = fetch_lfw_people(
        data_home="./data",
        min_faces_per_person=10,
        resize=1.0,
        color=True,
        download_if_missing=True
    )

    print("LFW downloaded successfully")
    print("Images:", len(dataset.images))
    print("Identities:", len(dataset.target_names))
    print("Image shape:", dataset.images.shape[1:])

if __name__ == "__main__":
    main()
