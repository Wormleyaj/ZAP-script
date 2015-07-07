from  org.zaproxy.clientapi.gen import Autoupdate
from org.zaproxy.zap.extension.autoupdate import AutoUpdateAPI
from org.zaproxy.clientapi.core import ClientApi
from org.zaproxy.zap.control import AddOnClassLoader
from org.zaproxy.zap.extension.autoupdate import ExtensionAutoUpdate


API =  ClientApi("localhost",8080)

Updater = Autoupdate(API)
Updater.setOptionInstallAddonUpdates("",True)

ExtensionUpdater =  ExtensionAutoUpdate()
API2 = AutoUpdateAPI(ExtensionUpdater)
ExtensionUpdater.installNewExtensions()
Updater.downloadLatestRelease("")
print API2.downloadLatestRelease()
print API2.getPrefix()
print API2.getLatestVersionNumber()
print "update complete"


