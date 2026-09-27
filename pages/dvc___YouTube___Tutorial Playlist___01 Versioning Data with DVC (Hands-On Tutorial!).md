logseq-entity:: [[Logseq/Entity/YouTube]], [[Logseq/Entity/Series]]
date-created:: [[2020/09/30]]
readwise-link:: https://read.readwise.io/read/01m3h42dpwm0bs2r2pcy872cwh

- # [Versioning Data with DVC (Hands-On Tutorial!)](https://www.youtube.com/watch?v=kLKBcPonMYw)
	- The opening video in [[dvc/YouTube/Tutorial Playlist]] introduces how DVC extends Git projects to version large data and models stored outside the Git repository.
	- ## Notes
		- Initialize Git and DVC, obtain a sample dataset with `dvc get`, then use `dvc add` to create a small `.dvc` file that Git can track while ignoring the dataset itself.
		- Configure a DVC remote, push the dataset to it, and pull a copy after removing the local data and cache.
		- After changing the dataset, run `dvc add` again, commit the changed `.dvc` file, and push the new data. Checking out an earlier Git revision of that `.dvc` file and running `dvc checkout` restores the corresponding data version.
		- Git records the version history of the pointer files; DVC stores and retrieves the larger data. The same workflow also applies to models and other files.
	- ## Readwise highlights
		- `dvc get` retrieves a dataset from a DVC data registry.
		- `dvc remote add -d` configures a default storage remote; the tutorial demonstrates Google Drive.
		- Git tracks the `.dvc` metadata while DVC manages the large file in remote storage.
