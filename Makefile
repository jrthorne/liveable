ROUSER := jason
ROHOST := brunel.eng.unsw.edu.au
RODIR := /www

RSYNC_OPTIONS := --verbose \
	--checksum \
	--recursive \
	--links \
	--times \
	--perms \
	--cvs-exclude \
	--compress \
	--exclude-from=NOROLLOUT

.PHONY: all rollout committed update

all:

committed:
	@if [ `svn st | wc -l` -gt 0]; then\
		echo -en "\\033[1;31m"; \
		echo "  **********************************************";\
		echo "  you still have modified files not checked in";\
		echo "  **********************************************";\
		echo -en "\\033[0;39m";

	fi

update:
	svn up
	@if svn st | grep -q ^C ; then \
		echo -en "\\033[1;31m"; \
		echo "  *********************************"; \
		echo "  conflicts exist!"; \
		echo "  *********************************"; \
		echo -en "\\033[1;39m"; \
		false;\
	fi

rollout:
	rsync $(RSYNC_OPTIONS) ../built $(ROUSER)@$(ROHOST):$(RODIR)/
	@echo "\\033[1;32m"
	@echo "  =================================================="
	@echo -n "   Rollout time is "
	@date
	@echo "  =================================================="
	@echo "\\033[0;39m";
