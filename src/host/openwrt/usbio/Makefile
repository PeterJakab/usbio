include $(TOPDIR)/rules.mk
PKG_NAME:=usbio
PKG_RELEASE:=3
PKG_VERSION:=2.2
PKG_BUILD_DIR := $(BUILD_DIR)/$(PKG_NAME)
include $(INCLUDE_DIR)/package.mk

define Package/usbio
	SECTION:=utils
	CATEGORY:=Utilities
	TITLE:=USB GPIO port utility
	URL:=http://jap.hu/electronic/
	MAINTAINER:=Peter Jakab <el@jap.hu>
	DEPENDS:=+libusb-compat
endef
define Package/usbio/description
 Utility for setup/reading/writing the usbio GPIO port hardware
endef

define Build/Prepare
	mkdir -p $(PKG_BUILD_DIR)
	$(CP) ./src/* $(PKG_BUILD_DIR)/
endef

define Package/usbio/install
	$(INSTALL_DIR) $(1)/usr/bin
	$(INSTALL_BIN) $(PKG_BUILD_DIR)/controlio $(1)/usr/bin/
endef

$(eval $(call BuildPackage,usbio))
