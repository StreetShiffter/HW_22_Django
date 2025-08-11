class DatabaseRouter:
    """
    Направляет модели из приложения 'blog' в БД 'blog',
    остальные — в 'default'
    """
    route_app_labels = {'blog'}  # имя второго приложения

    def db_for_read(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return 'blog'
        return 'default'

    def db_for_write(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return 'blog'
        return 'default'

    def allow_relation(self, obj1, obj2, **hints):
        db_set = {'default', 'blog'}
        if obj1._state.db in db_set and obj2._state.db in db_set:
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == 'blog':
            return db == 'blog'
        if db == 'blog':
            return False  # все остальные приложения — не в blog_db
        return None