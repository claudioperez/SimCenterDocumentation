
SUBDIRS := $(wildcard WEUQ/*)
ZIPS := $(addsuffix .zip,$(SUBDIRS))
# ZIPS := $(addsuffix .zip,$(subst /,,$(SUBDIRS)))


all: $(SUBDIRS); $(info $$ZIPS are: [${ZIPS}])

$(SUBDIRS): 
	zip -r $(addsuffix .zip,$@) $@

zip: $(ZIPS)
