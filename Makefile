NAME = plugin.video.pulsar
GIT = git
GIT_VERSION = $(shell $(GIT) describe --always)
VERSION = $(shell cat VERSION)
ARCHS = windows_x86 darwin_x64 linux_x86 linux_x64 linux_arm android_arm
ZIP_SUFFIX = zip
ZIP_FILE = $(NAME)-$(VERSION).$(ZIP_SUFFIX)

all: clean zip

bootstraper:
	mkdir -p $(NAME)
	sed s/\$$VERSION/0.0.1/g < addon.xml.tpl > $(NAME)/addon.xml
	cp fanart.jpg $(NAME)
	cp icon.png $(NAME)
	zip -9 -r $(NAME).zip $(NAME)
	rm -rf $(NAME)

$(ZIP_FILE):
	git archive --format zip --prefix $(NAME)/ --output $(ZIP_FILE) HEAD
	mkdir -p $(NAME)/resources/bin
	ln -s `pwd`/addon.xml $(NAME)
	zip -9 -r -g $(ZIP_FILE) $(NAME)/addon.xml
	for arch in $(ARCHS); do \
		ln -s `pwd`/resources/bin/$$arch $(NAME)/resources/bin/$$arch; \
		zip -9 -r -g $(ZIP_FILE) $(NAME)/resources/bin/$$arch; \
	done
	rm -rf $(NAME)

zipfiles: addon.xml
	for arch in $(ARCHS); do \
		$(MAKE) zip ARCHS=$$arch ZIP_SUFFIX=$$arch.zip; \
	done

zip: $(ZIP_FILE)

clean:
	rm -rf $(NAME)
