from src.components.PEFile import PEFile
from src.components.Dumper import Dumper

twinuipcshell = PEFile(r"C:\Windows\System32\twinui.pcshell.dll")
actxprxy = PEFile(r"C:\Windows\System32\actxprxy.dll")

dump = Dumper(Dumper.Output.FILE, 'Win11-23H2-22631.3085', [twinuipcshell, actxprxy])

dump.description()

dump.guid('IID_IVirtualDesktopManagerInternal2')
dump.guid('IID_IVirtualDesktopManager')
dump.guid('IID_IVirtualDesktop2')
dump.guid('IID_IVirtualDesktopPinnedApps')
dump.guid('IID_IVirtualDesktopNotification')
dump.guid('IID_IVirtualDesktopNotificationService')

dump.vftable('IVirtualDesktopManagerInternal', '??_7CVirtualDesktopManager@@6BIVirtualDesktopManagerInternal2@@@')
dump.vftable('IVirtualDesktopManager', '??_7VirtualDesktopsApi@@6B@')
dump.vftable('IVirtualDesktop', '??_7CVirtualDesktop@@6B?$ChainInterfaces@UIVirtualDesktop2@@UIVirtualDesktop@@VNil@Details@WRL@Microsoft@@V3456@V3456@V3456@V3456@V3456@V3456@V3456@@WRL@Microsoft@@@')
dump.vftable('IVirtualDesktopPinnedApps', '??_7VirtualPinnedAppsHandler@@6B?$ChainInterfaces@UIVirtualDesktopPinnedAppsPrivate@@UIVirtualDesktopPinnedApps@@VNil@Details@WRL@Microsoft@@V3456@V3456@V3456@V3456@V3456@V3456@V3456@@WRL@Microsoft@@@')
dump.vftable('IVirtualDesktopNotificationService', '??_7CVirtualDesktopNotificationsDerived@@6B@')
dump.vftable('IVirtualDesktopNotification', '??_7CVirtualDesktopNotificationsDerived@@6BIVirtualDesktopNotification@@@')
