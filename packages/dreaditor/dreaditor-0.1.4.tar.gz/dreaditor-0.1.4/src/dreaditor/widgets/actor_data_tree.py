import logging

from PyQt5.QtWidgets import QTreeWidget, QTreeWidgetItem, QWidget

from dreaditor.actor import Actor


class ActorDataTreeWidget(QTreeWidget):
    brfld_node: QTreeWidgetItem

    def __init__(self, parent: QWidget | None = ...) -> None:
        super().__init__(parent)
        self.logger = logging.getLogger(type(self).__name__)
        self.setHeaderLabels(["name", "value"])
        self.setColumnCount(2)

    def LoadActor(self, actor: Actor):
        self.clear()

        # load the level data from the brfld
        top_actor = QTreeWidgetItem([actor.level_data.sName])
        level_data = QTreeWidgetItem(["Level Data"])
        self.AddKeysToActor(level_data, actor.level_data)
        top_actor.addChild(level_data)

        # load the bmsad components, actionsets, soundfx
        if actor.bmsad != None:
            bmsad = actor.bmsad
            bmsad_data = QTreeWidgetItem(["Actordef Data"])
            bmsad_comps = QTreeWidgetItem(["Components"])
            self.AddKeysToActor(bmsad_comps, bmsad.raw.components)
            bmsad_actionsets = QTreeWidgetItem(["Action Sets"])
            bmsad_actionsets.addChildren([QTreeWidgetItem(["", item]) for item in bmsad.raw.action_sets])
            bmsad_soundfx = QTreeWidgetItem(["Sound FX"])
            bmsad_soundfx.addChildren([QTreeWidgetItem(["", f"{item[0]} (VOL {item[1]})"]) for item in bmsad.raw.sound_fx])
            bmsad_data.addChildren([bmsad_comps, bmsad_actionsets, bmsad_soundfx])
            top_actor.addChild(bmsad_data)
        else:
            self.logger.warn("The BMSAD for actor %s/%s/%s cannot be accessed due to a bug in mercury-engine-data-structures",
                             actor.ref.layer, actor.ref.sublayer, actor.ref.name)

        self.addTopLevelItem(top_actor)
        self.expandAll()
        
    def AddKeysToActor(self, item: QTreeWidgetItem, val: dict):
        for k,v in val.items():
            if isinstance(v, dict):
                child = QTreeWidgetItem([k, ""])
                self.AddKeysToActor(child, v)
                item.addChild(child)
            
            elif isinstance(v, list):
                child = QTreeWidgetItem([k, ""])

                if len(v) > 0 and len(v) <= 4 and isinstance(v[0], int | float):
                    res = "["
                    for va in v:
                        res += "{:.3f}".format(va)
                        res += ", "
                    res = res[:-2] + "]"
                    item.addChild(QTreeWidgetItem([k, res]))
                else:
                    self.AddKeysToActor(child, { str(i): value for i, value in enumerate(v)})
                    item.addChild(child)
            
            else:
                item.addChild(QTreeWidgetItem([k, str(v)]))
