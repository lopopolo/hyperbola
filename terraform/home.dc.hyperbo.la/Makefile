.PHONY: sync \
    sync-local sync-local-movies sync-local-music \
    sync-s3 sync-s3-movies sync-s3-music

TODAY := $(shell date +\%Y-\%m-\%d)

all: sync

sync: sync-local sync-s3

sync-local: sync-local-movies sync-local-music

sync-local-movies:
	if [[ ! -L ./media/movies ]]; then exit 1; fi
	rsync -av --exclude ".*" "$(HOME)/Movies/" ./media/movies

sync-local-music:
	if [[ ! -L ./media/music ]]; then exit 1; fi
	if [[ ! -L ./media/backup ]]; then exit 1; fi
	rsync -azvh --exclude ".*" --delete --backup --backup-dir="$(PWD)/media/backup/$(TODAY)" \
	    "$(HOME)/Music/iTunes/iTunes Media/Music/" ./media/music

sync-s3: sync-s3-movies sync-s3-music

sync-s3-movies:
	aws s3 sync --sse AES256 --exclude ".*" ./media/movies s3://home-dc-hyperbola/movies/

sync-s3-music:
	aws s3 sync --sse AES256 --exclude ".*" ./media/music s3://home-dc-hyperbola/music/
