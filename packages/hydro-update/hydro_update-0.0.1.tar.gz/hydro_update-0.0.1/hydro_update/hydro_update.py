""" Les variables d’entrées sont à bien définir et les données à ordonnées suivants une disposition bien définie afin que le module effectue les opérations et retourne les valeurs mises à jour du système de prévision. Les données utilisées sont constituées des débits observés et les débits simulés issus du modèle de prévision Glofas. Elles sont disposées dans un tableau à m lignes et n colonnes qui est nommé « dfi » dont :
•	la première colonne comporte les dates de mise à jour ;
•	 la deuxième colonnes nommée(obs)  représente les observations en fonction desquels la mise à jour est exécutée ;
•	les colonnes suivantes représentent les prévisions issues du modèle de prévisions (Glofas) pour les pas de temps bien défini de 1 à n.
 """


def mise_a_jour(df):
    for col, obs in zip(df.columns[1:], range(0,len(df.columns)-1)):
        df[col] = df[col].shift(-1) - df[col] + df[df.columns[obs]]
        df[col] = df[col].fillna(df[df.columns[obs]]).round(2)
        df[col] = df[col].apply(lambda num: 0 if (num<=0) else num )
    return df