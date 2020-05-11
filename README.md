
Введение.
Программа подбора аналогов позволяет в автоматическом режиме получить информацию о стоимости комплектующих выпускаемых различными производителями и имеющие равнозначные технические характеристики, находящиеся как в общей базе 1С, так и на складе в свободном остатке. Т.е. провести моментальное маркетинговое исследование.
Как работает
В 1С (либо иной программе) в спецификации любого заказа, должен быть столбец - «Ключ». Представляющий из себя краткую характеристику основных свойств аппарата. Файлы «s28b» и «Подбор аналогов.exe» должны находится в одной папке
Запустив программу и выбрав соответствующий раздел, Вы можете сформировать ключ, переписывая значения из спецификации с помощью выпадающих списков. Далее нажав кнопку «Показать из базы», получите список со всей имеющейся номенклатурой соответствующей данному ключу. Аналогичная ситуация с кнопкой «Показать склад», выйдет список того что лежит на складе в свободном остатке.  Изменяя значения ключа, к примеру, кА можно проследить динамику изменения цен как в меньшую, так и в большую сторону. 
Также реализована возможность выбрать конкретного производителя. Для это из выпадающего списка выбирается производитель номенклатуры и нажимается кнопка «Фильтр по производителю».
При нажатии на кнопку “Сохранить”, в той же папке где находится программа, будет создан отчет по выборке в редактируемом формате. После просмотра данных, файл необходимо закрыть или переименовать, так как имена «Ответ Базы» и «Ответ Склада» зарезервированы в программе и файл будет перезаписан.



Пример. 
Заказ №###. (База данных демонстрационная, работают только ниже перечисленные ключи + 1C16AC10)
№ п/п	Артикул	Наименование материала	Ключ
1	IEKMVA20-1-016-C	Выкл. авт. ВА 47-29 1Р 16А 4,5кА х-ка С; ИЭК; (IEKMVA20-1-016-C); 33В	1C16AC4,5
2	ABB2CSG221180R1101
	Трансформатор тока CT4/800/5A, класс 0.5; (ABB2CSG221180R1101);	80050,5
3	KUR110570	Контактор ПМЛ-2100-25А-220AC-УХЛ4-Б-КЭАЗ; (KUR110570);	325AC220

Открываем программу, заходим в Автоматические выключатели модульного исполнения, формируем ключ и получаем результат.


Выбираем раздел Автоматические выключатели модульного исполнения


Переписываем ключ
 
Нажимаем нужную кнопку, можно сразу обе и получаем результат. Список формируется в порядке возрастания цен.
Дело за малом. Согласовать удешевление проекта с заказчиком.
 

