import matplotlib
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtPrintSupport import *
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from datetime import *

# 상세정보 Form
class Ui_detailDialog(QDialog):
    # Setup
    def __init__(self):
        super().__init__()
        self.setupUi()                  # 화면 레이아웃
        self.dataInitPrint()          # 회원정보 출력

    # 화면 레이아웃
    def setupUi(self):
        self.setFixedSize(dialog_Win_size_length, dialog_Win_size_height)  # 어떤 환경이던 Dialog 크기를 고정함

        self.setWindowFlag(Qt.WindowCloseButtonHint, False)              # Window창의 Close 버튼(x모양)를 Disable함
        self.setWindowFlag(Qt.WindowContextHelpButtonHint, False)        # Window창의 Question 버튼(?모양)를 Disable함
        self.setWindowIcon(QIcon("img/memo.png"))                     # Window창의 Title옆의 Icon 모양 Setting
        self.setStyleSheet("background: white")                          # Dialog의 배경색을 하얀색으로 설정
        self.setWindowTitle("상세 정보")

        # Title(상세 정보)
        self.titleLabel = QLabel(self)                                  # QDialog에 QLabel을 선언
        self.titleLabel.setGeometry(QRect(0, 20, 400, 60))              # 위치
        self.titleLabel.setText("상세 정보")
        self.titleLabel.setAlignment(Qt.AlignCenter)
        # Font 속성 //
        font = QFont()
        font.setFamily("에스코어 드림 8 Heavy")
        font.setPointSize(24)
        self.titleLabel.setFont(font)       # //

        self.deletebutton = QToolButton(self)
        self.deletebutton.show()
        self.deletebutton.setGeometry(QRect(350,10,35,35))
        self.deletebutton.setMaximumSize(QSize(35, 35))
        self.deletebutton.setToolTip("삭제")
        icon = QIcon()
        icon.addPixmap(QPixmap("img/trash.png"), QIcon.Normal, QIcon.Off)
        self.deletebutton.setCursor(QCursor(Qt.PointingHandCursor))  # Point Cursor가 손가락 Cursor로 변경
        self.deletebutton.setIcon(icon)
        self.deletebutton.setIconSize(QSize(35, 35))
        self.deletebutton.clicked.connect(self.deleteInfo)
        for i in range(0, len(member_dtl_info_arr)):
            if member_dtl_info_arr[i][0] == info_mbr_id:
                if member_dtl_info_arr[i][17] != " ":
                    self.deletebutton.hide()



        # (*)은 필수 입력 사항입니다
        self.directionLabel = QLabel(self)  # QDialog에 QLabel을 선언
        self.directionLabel.setGeometry(QRect(10, 100, 180, 15))  # 위치
        self.directionLabel.setText("(*)은 필수 입력사항입니다.")
        # Font 속성 //
        font = QFont()
        font.setFamily("에스코어 드림 6 Bold")
        font.setPointSize(9)
        self.directionLabel.setFont(font)  # //
        # Label Text의 색깔
        palette = QPalette()
        palette.setColor(QPalette.WindowText, Qt.red)
        self.directionLabel.setPalette(palette)

        # Label LayoutWidget
        self.labelLayoutWidget = QWidget(self)
        self.labelLayoutWidget.setGeometry(QRect(10, 130, 82, 400))     # 위치

        # Label Layout
        self.labelBoxLayout = QVBoxLayout(self.labelLayoutWidget)       # LabelLayout 선언
        self.labelBoxLayout.setContentsMargins(0, 0, 0, 0)              # Margin setting
        self.labelBoxLayout.setSpacing(12)                              # Label간 간격 setting

        label_arr = ["회원 정보", "생년월일    *", "성별", "이메일    *", "전화번호    *", "주소", "차량 번호", "락커 정보", "리그 등급"]

        for i in range(0, len(label_arr)):
            self.label = QLabel(self.labelLayoutWidget)  # LabelLayoutWidget에 이름 Label을 선언
            # Font 속성 //
            font = QFont()
            font.setFamily("에스코어 드림 6 Bold")
            font.setPointSize(11)
            self.label.setFont(font)  # //
            self.label.setText(label_arr[i])
            self.labelBoxLayout.addWidget(self.label)  # LabelLayout에 이름 Label을 삽입

        # Text LayoutWidget
        self.textLayoutWidget = QWidget(self)
        self.textLayoutWidget.setGeometry(QRect(110, 130, 261, 355))    # 위치

        # Text Layout
        self.textBoxLayout = QVBoxLayout(self.textLayoutWidget)         # TextLayout 선언
        self.textBoxLayout.setContentsMargins(0, 4, 0, 0)               # Margin setting
        self.textBoxLayout.setSpacing(15)                               # Text 간 간격

        # 이름 Input (Read-Only)
        self.nameLayout = QHBoxLayout(self.textLayoutWidget)
        self.nameLayout.setContentsMargins(0, 0, 0, 0)  # Margin setting
        self.nameLayout.setSpacing(0)

        self.idText = QLineEdit(self.textLayoutWidget)  # TextLayoutWidget에 이름 Input을 선언
        # Font 설정 //
        font = QFont()
        font.setFamily("에스코어 드림 4 Regular")
        font.setPointSize(11)
        self.idText.setFont(font)  # //
        self.idText.setReadOnly(True)
        self.idText.setStyleSheet("border : 0")  # 이름 Input의 border값을 0으로 설정
        self.idText.setText(str(info_mbr_id) + "        / ")  # 회원번호 / 이름
        self.nameLayout.addWidget(self.idText)

        self.nameText = QLineEdit(self.textLayoutWidget)                # TextLayoutWidget에 이름 Input을 선언
        # Font 설정 //
        font = QFont()
        font.setFamily("에스코어 드림 4 Regular")
        font.setPointSize(11)
        self.nameText.setFont(font)     # //
        for i in range(0, len(member_dtl_info_arr)):
            if member_dtl_info_arr[i][0] == info_mbr_id:
                if member_dtl_info_arr[i][17] != " ":
                    self.nameText.setReadOnly(True)                                 # Read-only setting
                    self.nameText.setStyleSheet("border : 0")                       # 이름 Input의 border값을 0으로 설정
                    break
        self.nameText.setText(str(info_name))  # 회원번호 / 이름
        self.nameLayout.addWidget(self.nameText)
        self.textBoxLayout.addLayout(self.nameLayout)                     # TextLayout에 이름 Input을 삽입

        # 생년월일 Input
        self.birthText = QLineEdit(self.textLayoutWidget)               # TextLayoutWidget에 생년월일 Input을 선언
        # Font 설정 //
        font = QFont()
        font.setFamily("에스코어 드림 4 Regular")
        font.setPointSize(10)
        self.birthText.setFont(font)     # //
        self.birthText.setPlaceholderText("yyyyMMdd")                   # 입력 가이드 (yyyyMMdd)
        self.textBoxLayout.addWidget(self.birthText)                    # TextLayout에 생년월일 Input을 삽입

        # GenderLayout
        self.genderBoxLayout = QHBoxLayout()                            # GenderLayout 선언

        # 남자 Radio Button
        self.maleRadio = QRadioButton(self.textLayoutWidget)            # TextLayoutWidget에 남자 Radio Button을 선언
        # Font 설정 //
        font = QFont()
        font.setFamily("에스코어 드림 4 Regular")
        font.setPointSize(10)
        self.maleRadio.setFont(font)    # //
        self.genderBoxLayout.addWidget(self.maleRadio)                  # GenderLayout에 남자 Radio Button을 삽입

        # 여자 Radio Button
        self.femaleRadio = QRadioButton(self.textLayoutWidget)          # TextLayoutWidget에 여자 Radio Button을 선언
        # Font 설정 //
        font = QFont()
        font.setFamily("에스코어 드림 4 Regular")
        font.setPointSize(10)
        self.femaleRadio.setFont(font)  # //
        self.genderBoxLayout.addWidget(self.femaleRadio)                # GenderLayout에 여자 Radio Button을 삽입
        self.textBoxLayout.addLayout(self.genderBoxLayout)              # TextLayout에 GenderLayout을 삽입

        # EmailLayout
        self.emailBoxLayout = QHBoxLayout()                             # EmailLayout 선언

        # 이메일 주소(아이디) Input
        self.emailAddressText = QLineEdit(self.textLayoutWidget)        # TextLayoutWidget에 아이디 Input을 선언
        # Font 설정 //
        font = QFont()
        font.setFamily("에스코어 드림 4 Regular")
        font.setPointSize(10)
        self.emailAddressText.setFont(font) # //
        self.emailBoxLayout.addWidget(self.emailAddressText)            # EmailLayout에 아이디 Input을 삽입
        # @
        self.emailConLabel = QLabel(self.textLayoutWidget)              # TextLayoutWidget에 '@'를 선언
        # Font 설정 //
        font = QFont()
        font.setFamily("에스코어 드림 4 Regular")
        font.setPointSize(10)
        self.emailConLabel.setFont(font)    # //
        self.emailBoxLayout.addWidget(self.emailConLabel)               # EmailLayout에 '@'를 삽입
        # 이메일 주소(Domain) Input
        self.emailDomainText = QLineEdit(self.textLayoutWidget)         # EmailLayout에 Domain Input을 삽입
        # Font 설정 //
        font = QFont()
        font.setFamily("에스코어 드림 4 Regular")
        font.setPointSize(10)
        self.emailDomainText.setFont(font)  # //
        self.emailBoxLayout.addWidget(self.emailDomainText)             # EmailLayout에 Domain Input을 삽입
        self.textBoxLayout.addLayout(self.emailBoxLayout)               # TextLayout에 EmailLayout을 삽입

        # 전화번호 Input
        self.phoneNumText = QLineEdit(self.textLayoutWidget)            # TextLayoutWidget에 전화번호 Input을 선언
        # Font 설정 //
        font = QFont()
        font.setFamily("에스코어 드림 4 Regular")
        font.setPointSize(10)
        self.phoneNumText.setFont(font)     # //
        self.phoneNumText.setPlaceholderText("'-'을 포함하여 입력해주세요")   # 입력 가이드 ('-'을 포함하여 입력해주세요)
        self.textBoxLayout.addWidget(self.phoneNumText)                     # TextLayout에 전화번호 Input을 삽입

        # 주소 Input
        self.addressText = QLineEdit(self.textLayoutWidget)             # TextLayoutWidget에 주소 Input을 선언
        # Font 설정 //
        font = QFont()
        font.setFamily("에스코어 드림 4 Regular")
        font.setPointSize(10)
        self.addressText.setFont(font)      # //
        self.textBoxLayout.addWidget(self.addressText)                  # TextLayout에 주소 Input을 삽입

        # 차량 번호 Input
        self.carText = QLineEdit(self.textLayoutWidget)                     # TextLayoutWidget에 차량 번호 Input을 선언
        # Font 설정 //
        font = QFont()
        font.setFamily("에스코어 드림 4 Regular")
        font.setPointSize(10)
        self.carText.setFont(font)          # //
        self.carText.setPlaceholderText("예시 : 12가/3456 (띄워쓰기 금지)")  # 입력 가이드 (예시 : 12가/3456 (띄워쓰기 금지))
        self.textBoxLayout.addWidget(self.carText)                          # TextLayout에 차량 번호 Input을 선언

        # 락커 정보 Input
        self.lockerText = QLineEdit(self.textLayoutWidget)              # TextLayoutWidget에 락커 정보 Input을 선언
        # Font 설정 //
        font = QFont()
        font.setFamily("에스코어 드림 4 Regular")
        font.setPointSize(10)
        self.lockerText.setFont(font)       # //
        self.lockerText.setPlaceholderText("락커번호/락커비밀번호")       # 입력 가이드 (락커번호/락커비밀번호)
        self.textBoxLayout.addWidget(self.lockerText)                    # TextLayout에 락커정보 Input을 선언

        # 리그 등급 Input(개월 수 선택 ComboBox)
        self.leagueComboBox = QComboBox(self)                            # 리그 등급 Input 선언
        self.leagueComboBox.setGeometry(QRect(110, 500, 60, 26))         # 위치
        # ComboBox Item 개수(9개)
        for i in range(1, 10):
            self.leagueComboBox.addItem("")
        # Font 설정 //
        font = QFont()
        font.setFamily("에스코어 드림 6 Bold")
        font.setPointSize(10)
        self.leagueComboBox.setFont(font)        # //

        self.excl_checkBox = QCheckBox(self)
        self.excl_checkBox.setGeometry(QRect(270, 500, 100, 20))
        font = QFont()
        font.setFamily("에스코어 드림 6 Bold")
        font.setPointSize(10)
        self.excl_checkBox.setChecked(info_outp_exclude)
        self.excl_checkBox.setText("출력제외")

        # Save, Cancel Button Setting
        self.buttonBox = QDialogButtonBox(self)  # Dialog 버튼 Setting
        self.buttonBox.setGeometry(QRect(10, 540, 345, 40))  # 위치
        self.buttonBox.setOrientation(Qt.Horizontal)  # 버튼들 수평으로 보임
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel | QDialogButtonBox.Save)  # Save, Cancel 버튼 설정
        self.buttonBox.button(QDialogButtonBox.Save).setText("변경")  # Save -> 변경
        self.buttonBox.button(QDialogButtonBox.Cancel).setText("취소")  # Cancel -> 취소

        # 이벤트 모음
        self.retranslateUi()                # Label 출력 이벤트
        self.buttonBox.accepted.connect(self.saveMember)        # 상세정보 변경 이벤트 연결
        self.buttonBox.rejected.connect(self.reject)            # 취소 이벤트 연결

    def deleteInfo(self):
        df_memo = pd.read_excel('table/memo.xlsx')
        df_col = list([col for col in df_memo])  # table의 Header
        df_del_row = df_memo[df_memo['회원번호'] == info_mbr_id]
        df_new = df_memo.drop(df_del_row.index)  # 회원번호가 일치하는 행 drop
        df_list = df_new.values.tolist()  # df_new pandas를 array 형태로 변경
        list.sort(df_list, key=lambda k: (k[0], k[5]))  # 회원번호를 기준으로 df_list을 sort
        df_memo = pd.DataFrame(df_list, columns=df_col)  # df_list를 pandas 형태로 변경

        df_col = list([col for col in df_member])  # table의 Header
        df_del_row = df_member[df_member['회원번호'] == info_mbr_id]  # 회원번호가 일치하는 행
        df_new = df_member.drop(df_del_row.index)  # 회원번호가 일치하는 행 drop
        df_list = df_new.values.tolist()  # df_new pandas를 array 형태로 변경
        list.sort(df_list, key=lambda k: k[0])  # 회원번호를 기준으로 df_list을 sort
        df = pd.DataFrame(df_list, columns=df_col)  # df_list를 pandas 형태로 변경

        Ui_MainWindow().message_box_2(QMessageBox.Warning, '확인', '정말 삭제하시겠습니까?\n삭제된 정보는 복원하실 수 없습니다.', '예', '아니오')
        if MsgBoxRtnSignal == 'Y':  # '예'를 누르면
            Ui_MainWindow().message_box_1(QMessageBox.NoIcon, '삭제 완료', '삭제되었습니다.', '확인', )  # 변경 Alert
            df_memo.to_excel('table/memo.xlsx', index=False)
            df.to_excel('table/member_list.xlsx', index=False)  # 'member_list'에 저장
            self.close()  # 상세정보 Form 닫음
        else:
            pass  # if문 무시

    # 이전 'member_list'에서 선택한 정보들을 가져온 'info' array를 상세정보 Dialog에 뿌려줌
    def dataInitPrint(self):
        # self.nameText.setText(str(info_mbr_id) + " / " + str(info_name))    # 회원번호 / 이름
        self.birthText.setText(str(info_birth_date))                          # 생년월일
        # 성별
        if info_sex == '남':              # 남성 일때
            self.maleRadio.click()       # 남성 Radio Button click
        elif info_sex == '여':            # 여성 일때
            self.femaleRadio.click()     # 여성 Radio Button click
        emailarr = str(info_email).split("@")                              # '@'을 기준으로 split
        self.emailAddressText.setText(emailarr[0])                      # 이메일 주소(아이디)
        self.emailDomainText.setText(emailarr[1])                       # 이메일 주소(Domain)
        self.phoneNumText.setText(str(info_phone_no))                         # 전화번호
        self.addressText.setText(str(info_addr))                          # 주소
        self.carText.setText(str(info_car_no))                              # 차량번호
        # 락커정보
        if info[8] == '' and info[9] == '':                 # 락커번호/비밀비밀번호 없으면
            locker = ''                                     # 빈칸
        else:                                               # 있으면
            locker = str(info[8]) + '/' + str(info[9])      # 락커번호/락커비밀번호 변수 전달
        self.lockerText.setText(locker)                                 # 락커번호/락커비밀번호
        self.leagueComboBox.setCurrentIndex(int(info[10] - 1))          # 리그 등급(index는 0부터 시작하기 때문에 1부터 시작
                                                                        # 하는 리그 등급에 맞춰서 -1을 함)

    # Label 출력 메소드
    def retranslateUi(self):
        _translate = QCoreApplication.translate
        self.maleRadio.setText(_translate("Dialog", "남"))
        self.femaleRadio.setText(_translate("Dialog", "여"))
        self.emailConLabel.setText(_translate("Dialog", "@"))
        # 리그 등급(1~9)
        for i in range(0, 9):
            self.leagueComboBox.setItemText(i, _translate("Dialog", str(i + 1)))

    # 상세정보 변경 event
    def saveMember(self):
        # 기본 변수 setting
        # 남,여 Radio Check Event //
        if self.maleRadio.isChecked():      # 남성 Radio Button 체크되어 있을때
            gender_type = '남'              # gender_type을 남성으로 선언
        if self.femaleRadio.isChecked():    # 여성 Radio Button 체크되어 있을때
            gender_type = '여'              # gender_type을 여성으로 선언      //
        phone_number = self.phoneNumText.text()                                     # 전화번호
        email = self.emailAddressText.text() + '@' + self.emailDomainText.text()    # 이메일(아이디 + '@' + Domain)

        # 필수 입력 사항 없을 경우 체크
        if self.nameText.text() == '' or self.birthText.text() == '' or phone_number == '' or email == '@':     # 없으면
            Ui_MainWindow().message_box_1(QMessageBox.Warning, '경고', '필수 입력사항을 확인해주세요.', '확인')   # 경고문 출력
        else:       # 있으면
            created_time = info_created_on                                  # 변경이기 때문에 생성일이 바뀌면 안되므로 기존 값 사용
            created_by = info_created_by                                    # 변경이기 때문에 생성자가 바뀌면 안되므로 기존 값 사용
            changed_time = datetime.today().strftime('%Y-%m-%d %H:%M:%S')   # 수정일(오늘)
            changed_by = 'admin'                                            # 수정자(admin)
            # 락커정보가 없을 때
            if self.lockerText.text() == '':                # 없을 때
                locker = ['','']                            # array[2] 선언
            else:                                           # 있을 때
                locker = self.lockerText.text().split('/')  # '/'을 기준으로 split

            if self.excl_checkBox.isChecked() == 0:         #출력제외 CheckBox가 " "인 경우
                exclude_chk_box = ' '
            else:                                           #출력제외 CheckBox가 "x"인 경우
                exclude_chk_box = 'x'

            # arr에 변경된 정보 담음([이름, 전화번호, 생년월일, 성별, 이메일, 주소, 차량번호, 락커번호, 락커비밀번호, 리그번호,
            #                        리그번호, 생성일, 생성자, 수정일, 수정자])
            arr = [self.nameText.text(), phone_number, self.birthText.text(), gender_type, email,
                   self.addressText.text(), self.carText.text(), locker[0], locker[1], str(self.leagueComboBox.currentText()),
                   exclude_chk_box, created_time, created_by, changed_time, global_changed_by]

            if self.nameText.text() != str(info_name):
                memo_title = "(시스템) 회원 이름 변경"
                content = changed_time + "에 회원이름이 \'" + info_name + "\'에서 \'" + self.nameText.text() + "\'으로 변경됨."
                created_time = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
                created_by = 'admin'
                memo_arr = [info_mbr_id, str(memo_title), str(content), created_time, created_by,
                            changed_time, changed_by]

                df_memo = pd.read_excel('table/memo.xlsx')
                df_col = list([col for col in df_memo])
                df_list = df_memo.values.tolist()
                df_list.append(memo_arr)

                list.sort(df_list, key=lambda k: (k[0], k[5]))
                df_memo = pd.DataFrame(df_list, columns=df_col)



            # 'member_list' excel에 값 저장
            df_col = list([col for col in df_member])                      # table의 Header
            df_del_row = df_member[df_member['회원번호'] == info_mbr_id]       # 회원번호가 일치하는 행
            df_arr = df_del_row.values.tolist()                         # df_del_row pandas를 array 형태로 변경
            arr.insert(0, df_arr[0][0])                                 # 회원번호를 arr의 처음부분에 insert(index = 0)
            df_new = df_member.drop(df_del_row.index)                      # 회원번호가 일치하는 행 drop
            df_list = df_new.values.tolist()                            # df_new pandas를 array 형태로 변경
            df_list.append(arr)                                         # 변경된 정보를 append함
            list.sort(df_list, key=lambda k: k[0])                      # 회원번호를 기준으로 df_list을 sort
            df = pd.DataFrame(df_list, columns=df_col)                  # df_list를 pandas 형태로 변경
            # 변경 MessageBox
            Ui_MainWindow().message_box_2(QMessageBox.Question, '확인', '변경하시겠습니까?', '예', '아니오')
            if MsgBoxRtnSignal == 'Y':      # '예'를 누르면
                Ui_MainWindow().message_box_1(QMessageBox.NoIcon, '변경 완료', '변경되었습니다.', '확인', )  # 변경 Alert
                if self.nameText.text() != str(info_name):
                    df_memo.to_excel('table/memo.xlsx', index=False)
                df.to_excel('table/member_list.xlsx', index=False)   # 'member_list'에 저장
                self.close()                # 상세정보 Form 닫음
            else:
                pass                        # if문 무시

# 회원권 등록 Form
class Ui_enrollDialog(QDialog):
    # Setup
    def __init__(self):
        super().__init__()
        self.dataInit()         # 데이터
        self.setupUi()          # 화면 레이아웃
        self.addEnroll()        # 회원권 추가 등록 시

    # 데이터
    def dataInit(self):
        # 기본 변수 Global setting
        global df_list_col, df_list

    # 화면 레이아웃
    def setupUi(self):
        self.setFixedSize(dialog_Win_size_length, dialog_Win_size_height)  # 어떤 환경이던 Dialog 크기를 고정함

        self.setWindowFlag(Qt.WindowCloseButtonHint, False)             # Window창의 Close 버튼(x모양)를 Disable함
        self.setWindowFlag(Qt.WindowContextHelpButtonHint, False)       # Window창의 Question 버튼(?모양)를 Disable함
        self.setWindowIcon(QIcon("img/submit.png"))                    # Window창의 Title옆의 Icon 모양 Setting
        self.setStyleSheet("background: white")                         # Dialog의 배경색을 하얀색으로 설정
        self.setWindowTitle("회원권 등록")

        # Title(상세 정보)
        self.titleLabel = QLabel(self)  # QDialog에 QLabel을 선언
        self.titleLabel.setGeometry(QRect(0, 20, 400, 60))  # 위치
        self.titleLabel.setText("회원권 등록")
        self.titleLabel.setAlignment(Qt.AlignCenter)
        # Font 속성 //
        font = QFont()
        font.setFamily("에스코어 드림 8 Heavy")
        font.setPointSize(24)
        self.titleLabel.setFont(font)  # //

        # Save, Cancel Button Setting
        self.buttonBox = QDialogButtonBox(self)  # Dialog 버튼 Setting
        self.buttonBox.setGeometry(QRect(10, 540, 345, 40))  # 위치
        self.buttonBox.setOrientation(Qt.Horizontal)  # 버튼들 수평으로 보임
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel | QDialogButtonBox.Save)  # Save, Cancel 버튼 설정
        self.buttonBox.button(QDialogButtonBox.Save).setText("확인")  # Save -> 변경
        self.buttonBox.button(QDialogButtonBox.Cancel).setText("취소")  # Cancel -> 취소
        self.buttonBox.accepted.connect(self.enrollMembership)  # 상세정보 변경 이벤트 연결
        self.buttonBox.rejected.connect(self.reject)  # 취소 이벤트 연결

        # Enroll LayoutWidget
        self.enrollLayoutWidget = QWidget(self)                         # Ui_enrollDialog에 enrollLayoutWidget을 선언
        self.enrollLayoutWidget.setGeometry(QRect(20, 120, 340, 280))    # 위치

        # Enroll GridLayout
        self.enrollGridLayout = QGridLayout(self.enrollLayoutWidget)           # enrollLayoutWidget에 enrollGridLayout을 선언
        self.enrollGridLayout.setSizeConstraint(QGridLayout.SetMinAndMaxSize)  # Minimum, maximum size setting
        self.enrollGridLayout.setContentsMargins(0, 0, 0, 0)                   # Margin setting
        self.enrollGridLayout.setSpacing(20)                                   # Text 간 간격

        label_arr = ["회원 정보", "기간", "결제 방법", "", "특별 할인", "최종 금액", "시작일", "종료일"]
        for i in range(0, len(label_arr)):
            self.label = QLabel(self.enrollLayoutWidget)  # enrollLayoutWidget에 label_arr[i] Label을 선언
            # Font 설정 //
            font = QFont()
            font.setFamily("에스코어 드림 6 Bold")
            font.setPointSize(11)
            self.label.setFont(font)  # //
            self.label.setText(label_arr[i])
            self.enrollGridLayout.addWidget(self.label, i, 0, 1, 1)  # enrollGridLayout(i,0)에 label_arr[i] Label을 삽입

        # 회원 아이디 Input
        self.memberIdText = QLabel(self.enrollLayoutWidget)  # enrollLayoutWidget에 회원 아이디 Input을 선언
        # Font 설정
        font = QFont()
        font.setFamily("에스코어 드림 6 Bold")
        font.setPointSize(10)
        self.memberIdText.setFont(font)  # //
        self.enrollGridLayout.addWidget(self.memberIdText, 0, 1, 1, 1)  # enrollGridLayout(0,1)에 회원 아이디 Input을 삽입

        # 회원 이름 Text
        self.memberNameText = QLabel(self)  # Ui_enrollDialog에 회원 이름 Text을 선언
        # Font 설정 //
        font = QFont()
        font.setFamily("에스코어 드림 6 Bold")
        font.setPointSize(10)
        self.memberNameText.setFont(font)  # //
        self.memberNameText.setGeometry(QRect(220, 125, 60, 16))  # 위치

        # 개월 선택 ComboBox
        self.monthChangeComboBox = QComboBox(self.enrollLayoutWidget)  # enrollLayoutWidget에 개월 선택 Combox을 선언
        # ComboBox Item 갯수 = 3 //
        month_counter = 0
        for i in range(0, 5):
            comboBox_month = df_global_col[i + 9].split(' ')
            if df_global_list[0][i + 9] != ' ':
                self.monthChangeComboBox.addItem("")  # //
                self.monthChangeComboBox.setItemText(month_counter, comboBox_month[0])
                month_counter += 1
        # Font 설정 //
        font = QFont()
        font.setFamily("에스코어 드림 6 Bold")
        font.setPointSize(10)
        self.monthChangeComboBox.setFont(font)  # //
        self.monthChangeComboBox.activated.connect(self.onActivated)
        self.enrollGridLayout.addWidget(self.monthChangeComboBox, 1, 1, 1, 1)  # enrollGridLayout(1,1)에 개월 선택 ComboBox을 삽입

        # 결제 방법 Layout
        self.rb_groupBox_1 = QButtonGroup(self)

        self.payBoxLayout = QHBoxLayout()

        # 최종 금액 Text
        self.totalCostText = QLabel(self.enrollLayoutWidget)  # enrollLayoutWidget에 최종 금액 Text을 선언
        # Font 설정 //
        font = QFont()
        font.setFamily("에스코어 드림 6 Bold")
        font.setPointSize(10)
        self.totalCostText.setFont(font)  # //
        self.enrollGridLayout.addWidget(self.totalCostText, 5, 1, 1, 1)  # enrollGridLayout(3,1)에 최종 금액 Text을 삽입

        # 카드 Radio Button
        self.cardRadioButton = QRadioButton(self.enrollLayoutWidget)  # enrollLayoutWidget에 카드 Radio Button을 선언
        # Font 설정 //
        font = QFont()
        font.setFamily("에스코어 드림 6 Bold")
        font.setPointSize(10)
        self.cardRadioButton.setFont(font)  # //
        self.payBoxLayout.addWidget(self.cardRadioButton)  # 결제 방법 Layout에 카드 Radio Button을 삽입
        self.rb_groupBox_1.addButton(self.cardRadioButton)

        # 현금 Radio Button
        self.cashRadioButton = QRadioButton(self.enrollLayoutWidget)  # enrollLayoutWidget에 현금 Radio Button을 선언
        # Font 설정 //
        font = QFont()
        font.setFamily("에스코어 드림 6 Bold")
        font.setPointSize(10)
        self.cashRadioButton.setFont(font)  # //
        self.rb_groupBox_1.addButton(self.cashRadioButton)
        self.payBoxLayout.addWidget(self.cashRadioButton)  # 결제 방법 Layout에 현금 Radio Button을 삽입

        self.enrollGridLayout.addLayout(self.payBoxLayout, 2, 1, 1, 1)  # enrollGridLayout(2,1)에 결제 방법 Layout을 삽입

        # 결제 방법 Layout
        self.ageLayout = QHBoxLayout()
        self.rb_groupBox_2 = QButtonGroup(self)

        # 카드 Radio Button
        self.normalRadioButton = QRadioButton(self)  # enrollLayoutWidget에 카드 Radio Button을 선언

        # Font 설정 //
        font = QFont()
        font.setFamily("에스코어 드림 6 Bold")
        font.setPointSize(10)
        self.normalRadioButton.setFont(font)  # //
        self.ageLayout.addWidget(self.normalRadioButton)  # 결제 방법 Layout에 카드 Radio Button을 삽입
        self.rb_groupBox_2.addButton(self.normalRadioButton)

        # 현금 Radio Button
        self.teenRadioButton = QRadioButton(self)  # enrollLayoutWidget에 현금 Radio Button을 선언

        # Font 설정 //
        font = QFont()
        font.setFamily("에스코어 드림 6 Bold")
        font.setPointSize(10)
        self.teenRadioButton.setFont(font)  # //
        self.rb_groupBox_2.addButton(self.teenRadioButton)
        self.ageLayout.addWidget(self.teenRadioButton)  # 결제 방법 Layout에 현금 Radio Button을 삽입
        self.enrollGridLayout.addLayout(self.ageLayout, 3, 1, 1, 1)  # enrollGridLayout(2,1)에 결제 방법 Layout을 삽입

        self.specialDiscountLayout = QHBoxLayout()

        self.specialDiscountCheckbox = QCheckBox(self.enrollLayoutWidget)
        font = QFont()
        font.setFamily("에스코어 드림 6 Bold")
        font.setPointSize(10)
        self.specialDiscountCheckbox.setFont(font)  # //
        self.specialDiscountCheckbox.clicked.connect(self.discountClicked)

        self.specialDiscountLayout.addWidget(self.specialDiscountCheckbox)  # 결제 방법 Layout에 현금 Radio Button을 삽입

        self.specialDisountLabel = QLineEdit(self.enrollLayoutWidget)
        font = QFont()
        font.setFamily("에스코어 드림 6 Bold")
        font.setPointSize(10)
        self.specialDisountLabel.setFont(font)  # //
        self.specialDisountLabel.setText("")
        self.specialDisountLabel.setValidator(QRegExpValidator(QRegExp("[0-9]{5}")))
        self.specialDisountLabel.setReadOnly(True)
        self.specialDisountLabel.setStyleSheet("background-color: lightgray")
        self.specialDiscountLayout.addWidget(self.specialDisountLabel)
        self.specialDisountLabel.setPlaceholderText("(원)")
        self.specialDisountLabel.textChanged.connect(self.specialDiscount)
        self.enrollGridLayout.addLayout(self.specialDiscountLayout, 4, 1, 1, 1)

        # 시작일 Input
        self.startDateEdit = QDateEdit(self.enrollLayoutWidget)  # enrollLayoutWidget에 시작일 Input을 선언
        # Font 설정 //
        font = QFont()
        font.setFamily("에스코어 드림 6 Bold")
        font.setPointSize(10)
        self.startDateEdit.setFont(font)  # //
        self.startDateEdit.setDate(date.today())  # 시작일 Input을 오늘로 설정
        self.startDateEdit.setCalendarPopup(True)  # 시작일 Input을 캘린더 모드로 지정
        self.startDateEdit.dateChanged.connect(self.startDateChange)
        self.enrollGridLayout.addWidget(self.startDateEdit, 6, 1, 1, 1)  # enrollGridLayout(4,1)에 시작일 Input을 삽입

        # 종료일 Input
        self.endDateEdit = QDateEdit(self.enrollLayoutWidget)  # enrollLayoutWidget에 종료일 Input을 선언
        # Font 설정 //
        font = QFont()
        font.setFamily("에스코어 드림 6 Bold")
        font.setPointSize(10)
        self.endDateEdit.setFont(font)  # //
        self.endDateEdit.setCalendarPopup(True)  # 종료일 Input을 캘린더 모드로 지정
        self.enrollGridLayout.addWidget(self.endDateEdit, 7, 1, 1, 1)

        self.retranslateUi()

        self.cardRadioButton.clicked.connect(self.cardClick)
        self.cardRadioButton.click()
        self.cashRadioButton.clicked.connect(self.cashClick)
        self.normalRadioButton.clicked.connect(self.normalClick)
        self.normalRadioButton.click()
        self.teenRadioButton.clicked.connect(self.teenClick)

    # 특별할인 적용에 따른 금액 계산
    def specialDiscount(self):
        for i in range(0, len(month_type_arr)):
            if str(self.monthChangeComboBox.currentText()) == month_type_arr[i]:
                money = fee_by_type_arr[i]                  # fee_by_type_arr[i]: 1, 3, 6, 9, 12개월치 요금
                if self.cashRadioButton.isChecked():
                    money -= fee_dscnt_by_type_arr[i]       # fee_dscnt_by_type_arr[i]: 1, 3, 6, 9, 12개월치 할인액
                if self.teenRadioButton.isChecked():
                    money = int(money * final_teen_discounted)   # final_teen_discounted: 청소년할인 적용 후 최종 금액 적용율
                if self.specialDisountLabel.text() == "":
                    special_discount = 0
                else:
                    special_discount = self.specialDisountLabel.text()
                money -= int(special_discount)
                self.totalCostText.setText(str(money) + "원")

    # 특별할인 체크박스에 체크가 된경우 배경색 흰색, 입력가능이고 안된경우 회색, 입력불가 모드로 전환
    def discountClicked(self):
        if self.specialDiscountCheckbox.isChecked():
            self.specialDisountLabel.setReadOnly(False)
            self.specialDisountLabel.setStyleSheet("background-color: white")
            self.specialDisountLabel.setText("0")
        else:
            self.specialDisountLabel.setReadOnly(True)
            self.specialDisountLabel.setStyleSheet("background-color: lightgray")
            self.specialDisountLabel.setText("")

    # 일반회원 대한 금액계산
    def normalClick(self):
        for i in range(0, len(month_type_arr)):
            if str(self.monthChangeComboBox.currentText()) == month_type_arr[i]:
                money = fee_by_type_arr[i]                  # fee_by_type_arr[i]: 1, 3, 6, 9, 12개월치 요금
                if self.cashRadioButton.isChecked():
                    money -= fee_dscnt_by_type_arr[i]       # fee_dscnt_by_type_arr[i]: 1, 3, 6, 9, 12개월치 할인액
                if self.specialDiscountCheckbox.isChecked():
                    if self.specialDisountLabel.text() == "":
                        special_discount = 0
                    else:
                        special_discount = self.specialDisountLabel.text()
                    money -= int(special_discount)
                self.totalCostText.setText(str(money) + "원")

    # 청소년회원(할인적용)에 대한 금액계산
    def teenClick(self):
        for i in range(0,len(month_type_arr)):
            if str(self.monthChangeComboBox.currentText()) == month_type_arr[i]:
                money = fee_by_type_arr[i]                  # fee_by_type_arr[i]: 1, 3, 6, 9, 12개월치 요금
                if self.cashRadioButton.isChecked():
                    money -= fee_dscnt_by_type_arr[i]       # fee_dscnt_by_type_arr[i]: 1, 3, 6, 9, 12개월치 할인액
                money = int(money * final_teen_discounted)      # final_teen_discounted: 청소년할인 적용 후 최종 금액 적용율
                if self.specialDiscountCheckbox.isChecked():
                    if self.specialDisountLabel.text() == "":
                        special_discount = 0
                    else:
                        special_discount = self.specialDisountLabel.text()
                    money -= int(special_discount)
                self.totalCostText.setText(str(money) + "원")

    # 회원권이 남아있을 때 추가 등록하는 경우
    def addEnroll(self):
        if info_start_date != '' and info_end_date != '':
            self.startDateEdit.setDate(QDate.fromString(info_end_date, "yyyy-MM-dd").addDays(1))
            start_date = self.startDateEdit.date()
            self.endDateEdit.setDate(start_date.addMonths(1).addDays(-1))
        self.memberIdText.setText(str(info_mbr_id))  # 회원 ID 출력
        self.memberNameText.setText(info_name)  # 회원 이름 출력
        self.totalCostText.setText(str(fee_by_type_arr[0]) + "원")  # fee_by_type_arr[0]: 1개월 요금

    # 개월 선택 event
    def onActivated(self):
        start_date = self.startDateEdit.date()
        for i in range(0, len(month_type_arr)):
            if str(self.monthChangeComboBox.currentText()) == month_type_arr[i]:
                add_month = month_type_arr[i].split('개')
                add_month = add_month[0]
                money = fee_by_type_arr[i]                  # fee_by_type_arr[i]: 1, 3, 6, 9, 12개월치 요금
                if self.cashRadioButton.isChecked():
                    money -= fee_dscnt_by_type_arr[i]       # fee_dscnt_by_type_arr[i]: 1, 3, 6, 9, 12개월치 할인액
                if self.teenRadioButton.isChecked():
                    money = int(money * final_teen_discounted)   # final_teen_discounted: 청소년할인 적용 후 최종 금액 적용율
                if self.specialDiscountCheckbox.isChecked():
                    money -= int(self.specialDisountLabel.text())
                self.totalCostText.setText(str(money) + "원")
                self.endDateEdit.setDate(start_date.addMonths(int(add_month)).addDays(-1))

    # 결제 방법 Radio event(카드)
    def cardClick(self):
        for i in range(0, len(month_type_arr)):
            if str(self.monthChangeComboBox.currentText()) == month_type_arr[i]:
                money = df_global_list[0][i + 9]
                if self.teenRadioButton.isChecked():
                    money = int(money * final_teen_discounted)   # final_teen_discounted: 청소년할인 적용 후 최종 금액 적용율
                if self.specialDiscountCheckbox.isChecked():
                    if self.specialDisountLabel.text() == "":
                        special_discount = 0
                    else:
                        special_discount = self.specialDisountLabel.text()
                    money -= int(special_discount)
                self.totalCostText.setText(str(money) + "원")

    # 결제 방법 Radio event(현금)
    def cashClick(self):
        for i in range(0, len(month_type_arr)):            # month_type_arr["1개월", "3개월", "6개월", "9개월", "12개월"]
            if str(self.monthChangeComboBox.currentText()) == month_type_arr[i]:
                money = fee_by_type_arr[i] - fee_dscnt_by_type_arr[i]   # 각 (1, 3, 6, 9, 12개월치 요금) - (1, 3, 6, 9, 12개월치 할인액)
                if self.teenRadioButton.isChecked():
                    money = int(money * final_teen_discounted)   # final_teen_discounted: 청소년할인 적용 후 최종 금액 적용율
                if self.specialDiscountCheckbox.isChecked():
                    if self.specialDisountLabel.text() == "":
                        special_discount = 0
                    else:
                        special_discount = self.specialDisountLabel.text()
                    money -= int(special_discount)
                self.totalCostText.setText(str(money) + "원")

    # 시작일 변경 event
    def startDateChange(self):
        start_date = self.startDateEdit.date()
        for i in range(0, len(month_type_arr)):
            if str(self.monthChangeComboBox.currentText()) == month_type_arr[i]:
                add_month = month_type_arr[i].split('개')
                add_month = add_month[0]
                self.endDateEdit.setDate(start_date.addMonths(int(add_month)).addDays(-1))

    # 회원권 등록 event
    def enrollMembership(self):
        # 기본 변수 setting
        start_date = self.startDateEdit.date()
        end_date = self.endDateEdit.date()
        member_num = self.memberIdText.text()
        created_time = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
        changed_time = datetime.today().strftime('%Y-%m-%d %H:%M:%S')

        df_col = list([col for col in df_enroll])
        df_counter_row = df_enroll[df_enroll['회원번호'] == int(member_num)]
        df_selected_member = df_counter_row.values.tolist()

        # enroll_arr Table에 들어갈 행
        enroll_arr = [int(member_num), len(df_selected_member) + 1, QDate.toString(start_date, 'yyyy-MM-dd'), QDate.toString(end_date, 'yyyy-MM-dd'), "","",
                      created_time, global_created_by, changed_time, global_changed_by]


        df_list = df_enroll.values.tolist()
        df_list.append(enroll_arr)

        list.sort(df_list, key=lambda k: (k[0], k[1]))
        df = pd.DataFrame(df_list, columns=df_col)

        df_memo = pd.read_excel('table/memo.xlsx')
        df_memo_col = list([col for col in df_memo])
        df_memo_row = df_memo[df_memo['회원번호'] == int(member_num)]
        df_memo_row_list = df_memo_row.values.tolist()
        df_memo_list = df_memo.values.tolist()
        if self.specialDisountLabel.text() == "":
            spcl_discount_amt = "0"
        else:
            spcl_discount_amt = self.specialDisountLabel.text()
        memo_content = "결제 : " + self.rb_groupBox_1.checkedButton().text() + "/" + self.rb_groupBox_2.checkedButton().text() + \
                        "/" + "특별 할인(" + spcl_discount_amt + "원)" + "/" + "최종 금액(" + \
                        self.totalCostText.text() + ")\n" + QDate.toString(start_date, 'yyyy-MM-dd') + " ~ " + \
                       QDate.toString(end_date, 'yyyy-MM-dd') + " 기간의 회원권을 등록함."
        df_pause_arr = [int(member_num), "(시스템) 회원권 등록 내역", memo_content,
                        created_time, global_created_by, changed_time, global_changed_by]
        df_memo_list.append(df_pause_arr)
        list.sort(df_memo_list, key=lambda k: (k[0], k[5]))
        df_memo = pd.DataFrame(df_memo_list, columns=df_memo_col)

        Ui_MainWindow().message_box_2(QMessageBox.Question, '확인', '등록하시겠습니까?', '예', '아니오')
        if MsgBoxRtnSignal == 'Y':
            Ui_MainWindow().message_box_1(QMessageBox.NoIcon, '등록 완료', '등록되었습니다.', '확인', )
            df.to_excel('table/enroll_list.xlsx', index=False)
            df_memo.to_excel('table/memo.xlsx', index=False)
            self.close()
        else:
            pass

    # Label 출력
    def retranslateUi(self):
        _translate = QCoreApplication.translate
        self.cardRadioButton.setText(_translate("Dialog", "카드"))
        self.cashRadioButton.setText(_translate("Dialog", "현금"))
        self.normalRadioButton.setText(_translate("Dialog", "일반"))
        self.teenRadioButton.setText(_translate("Dialog", "청소년"))

# 회원권 양도 Form
class Ui_transferDialog(QDialog):
    # Setup
    def __init__(self):
        super().__init__()
        self.get_init_data()
        self.setupUi()

    def get_init_data(self):
        global give_date_start, give_date_end, days_left, take_date_start, take_date_end
        # info_QDate_start : enroll_list 기간 시작, info_QDate_end : enroll_list 기간 종료,
        # pause_date_start : 정지 시작일(고정값 변경 불가), pause_date_end = 정지 종료일,
        # new_date_start : 재 시작일(무조건 pause_date_end의 다음날),
        # new_date_end : 재 종료일(재 시작일 + (info_QDate_end - pause_date_start))

        if today_QDate >= info_QDate_start:
            give_date_start = today_QDate.addDays(1)
        else:
            give_date_start = info_QDate_start
        days_left = give_date_start.daysTo(info_QDate_end)
        give_date_end = info_QDate_end
        take_date_start = QDate.toString(give_date_start, 'yyyy-MM-dd')
        take_date_end = QDate.toString(give_date_start.addDays(int(days_left)), 'yyyy-MM-dd')

    # 화면 레이아웃
    def setupUi(self):
        self.setFixedSize(dialog_Win_size_length, dialog_Win_size_height)  # 어떤 환경이던 Dialog 크기를 고정함

        self.setWindowFlag(Qt.WindowCloseButtonHint, False)             # Window창의 Close 버튼(x모양)를 Disable함
        self.setWindowFlag(Qt.WindowContextHelpButtonHint, False)       # Window창의 Question 버튼(?모양)를 Disable함
        self.setWindowIcon(QIcon("img/give-money.png"))                    # Window창의 Title옆의 Icon 모양 Setting
        self.setStyleSheet("background: white")                         # Dialog의 배경색을 하얀색으로 설정
        self.setWindowTitle("회원권 양도")

        # Title(상세 정보)
        self.titleLabel = QLabel(self)  # QDialog에 QLabel을 선언
        self.titleLabel.setGeometry(QRect(0, 20, 400, 60))  # 위치
        self.titleLabel.setText("회원권 양도")
        self.titleLabel.setAlignment(Qt.AlignCenter)
        # Font 속성 //
        font = QFont()
        font.setFamily("에스코어 드림 8 Heavy")
        font.setPointSize(24)
        self.titleLabel.setFont(font)  # //

        # Save, Cancel Button Setting
        self.buttonBox = QDialogButtonBox(self)  # Dialog 버튼 Setting
        self.buttonBox.setGeometry(QRect(10, 540, 345, 40))  # 위치
        self.buttonBox.setOrientation(Qt.Horizontal)  # 버튼들 수평으로 보임
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel | QDialogButtonBox.Save)  # Save, Cancel 버튼 설정
        self.buttonBox.button(QDialogButtonBox.Save).setText("확인")  # Save -> 변경
        self.buttonBox.button(QDialogButtonBox.Cancel).setText("취소")  # Cancel -> 취소
        self.buttonBox.accepted.connect(self.transferMembership)  # 회원권 양도 이벤트 연결
        self.buttonBox.rejected.connect(self.reject)  # 취소 이벤트 연결

        # Layout
        self.gridLayoutWidget = QWidget(self)
        self.gridLayoutWidget.setGeometry(QRect(20, 100, 360, 250))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        # self.gridLayout.setSizeConstraint(QGridLayout.SetMinAndMaxSize)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(20)

        label_arr = ["회원정보", "양도 시작일", "양도 종료일", "양수자", "양수 시작일", "양수 종료일"]
        for i in range(0, len(label_arr)):
            self.label = QLabel(self.gridLayoutWidget)
            font = QFont()
            font.setFamily("에스코어 드림 6 Bold")
            font.setPointSize(11)
            self.label.setFont(font)
            self.label.setText(label_arr[i])
            self.gridLayout.addWidget(self.label, i, 0, 1, 1)

        # 회원정보 Data
        self.mbrInfoValueLabel = QLabel(self.gridLayoutWidget)  # QDialog에 QLabel을 선언
        # Font 속성 //
        font = QFont()
        font.setFamily("에스코어 드림 6 Bold")
        font.setPointSize(10)
        self.mbrInfoValueLabel.setFont(font)
        self.mbrInfoValueLabel.setText(str(info_mbr_id) + " / " + str(info_name))  # 회원번호 / 이름
        self.gridLayout.addWidget(self.mbrInfoValueLabel, 0, 1, 1, 1)

        # 양도시작일 DateEdit
        self.startDateEdit = QDateEdit(self.gridLayoutWidget)
        font = QFont()
        font.setFamily("에스코어 드림 6 Bold")
        font.setPointSize(10)
        self.startDateEdit.setFont(font)
        self.startDateEdit.setReadOnly(True)
        self.startDateEdit.setCalendarPopup(True)
        self.startDateEdit.setDate(give_date_start)
        self.gridLayout.addWidget(self.startDateEdit, 1, 1, 1, 1)

        # 양도종료일 DateEdit
        self.endDateEdit = QDateEdit(self.gridLayoutWidget)
        font = QFont()
        font.setFamily("에스코어 드림 6 Bold")
        font.setPointSize(10)
        self.endDateEdit.setFont(font)
        self.endDateEdit.setCalendarPopup(True)
        self.endDateEdit.setReadOnly(True)
        self.endDateEdit.setDate(give_date_end)
        self.gridLayout.addWidget(self.endDateEdit, 2, 1, 1, 1)

        # 양수자 회원번호
        self.receiver_id = QLineEdit(self.gridLayoutWidget)
        font = QFont()
        font.setFamily("에스코어 드림 6 Bold")
        font.setPointSize(10)
        self.receiver_id.setFont(font)
        self.receiver_id.setValidator(QRegExpValidator(QRegExp("[0-9]{5}")))
        self.receiver_id.textChanged.connect(self.transferName)
        self.gridLayout.addWidget(self.receiver_id, 3, 1, 1, 1)

        # 양수자 이름
        self.receiver_name = QTextEdit(self.gridLayoutWidget)
        font = QFont()
        font.setFamily("에스코어 드림 6 Bold")
        font.setPointSize(10)
        self.receiver_name.setFont(font)
        self.receiver_name.setReadOnly(True)
        self.receiver_name.setStyleSheet("border : 0")
        self.receiver_name.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.gridLayout.addWidget(self.receiver_name, 3, 2, 1, 1)

        # 양수 시작일
        self.recv_str_date = QTextEdit(self.gridLayoutWidget)
        font = QFont()
        font.setFamily("에스코어 드림 6 Bold")
        font.setPointSize(10)
        self.recv_str_date.setReadOnly(True)
        self.recv_str_date.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.recv_str_date.setFont(font)
        self.recv_str_date.setStyleSheet("border : 0")
        self.recv_str_date.setText(take_date_start)
        self.gridLayout.addWidget(self.recv_str_date, 4, 1, 1, 1)

        # 양수 종료일
        self.recv_end_date = QTextEdit(self.gridLayoutWidget)
        font = QFont()
        font.setFamily("에스코어 드림 6 Bold")
        font.setPointSize(10)
        self.recv_end_date.setReadOnly(True)
        self.recv_end_date.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.recv_end_date.setFont(font)
        self.recv_end_date.setObjectName("pause_date_1")
        self.recv_end_date.setStyleSheet("border : 0")
        self.recv_end_date.setText(take_date_end)
        self.gridLayout.addWidget(self.recv_end_date, 5, 1, 1, 1)

        # 양도 사유 Label
        self.label = QLabel(self)
        self.label.setGeometry(QRect(20, 410, 80, 30))
        font = QFont()
        font.setFamily("에스코어 드림 6 Bold")
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setText("양도사유")

        # 양도사유 입력
        self.reasonText = QLineEdit(self)
        self.reasonText.setGeometry(QRect(30, 455, 340, 30))
        font = QFont()
        font.setFamily("에스코어 드림 4 Regular")
        font.setPointSize(10)
        self.reasonText.setFont(font)

        self.retranslateUi()

    # 양수인 ID(receiver_id)가 입력되면 양수인 이름(receiver_name) 자동지정
    def transferName(self):
        if self.receiver_id.text() == '':
            member_num = 0
        else:
            member_num = int(self.receiver_id.text())
        df_member_row = df_merge[df_merge['회원번호'] == member_num]
        df_selected_member = df_member_row.values.tolist()

        if len(df_selected_member) >= 1:              # 회원 ID당 여러개의 회원권 등록 이력이 있을 수 있음
            df_selected_member.reverse()  # 역 Sort를 통해 가장 최신의 회원권 등록 이력이 맨위로
            if df_selected_member[0][17] != ' ' and df_selected_member[0][18] != ' ':        # 무조건 신규회원이 아님(회원권 시작일, 회원권 종료일)
                self.receiver_name.setText(df_selected_member[0][1])
                start_date = QDate.fromString(df_selected_member[0][17], "yyyy-MM-dd")  # 최신 회원권 시작일
                end_date = QDate.fromString(df_selected_member[0][18], "yyyy-MM-dd")    # 최신 회원권 종료일
                days_left = self.startDateEdit.date().daysTo(self.endDateEdit.date()) # 잔여일수는 종료일과 오늘의 일수 차이
                if QDate.fromString(df_selected_member[0][18], "yyyy-MM-dd") < today_QDate:
                    self.recv_str_date.setText(QDate.toString(today_QDate.addDays(1), 'yyyy-MM-dd'))
                    self.recv_end_date.setText(QDate.toString(today_QDate.addDays(int(days_left) + 1), 'yyyy-MM-dd'))
                else:
                    self.recv_str_date.setText(QDate.toString(end_date.addDays(1), 'yyyy-MM-dd'))
                    self.recv_end_date.setText(QDate.toString(end_date.addDays(int(days_left) + 1), 'yyyy-MM-dd'))
            else:                                                 # 신규회원
                self.receiver_name.setText(df_selected_member[0][1])
                self.recv_str_date.setText(QDate.toString(today_QDate.addDays(1), 'yyyy-MM-dd'))

                if today_QDate < info_QDate_start:
                    days_left = info_QDate_start.daysTo(info_QDate_end)
                    self.recv_end_date.setText(QDate.toString(today_QDate.addDays(int(days_left) + 1), 'yyyy-MM-dd'))
                else:
                    give_start_date = self.startDateEdit.date()
                    days_left = give_start_date.daysTo(info_QDate_end)
                    self.recv_end_date.setText(QDate.toString(today_QDate.addDays(int(days_left) + 1), 'yyyy-MM-dd'))
        else:
            self.receiver_name.setText("")

    # 회원권 양도 event
    def transferMembership(self):
        if self.receiver_name.toPlainText() == '':
            Ui_MainWindow().message_box_1(QMessageBox.Warning, '경고', '양수자 정보를 다시 확인해주세요', '확인', )
        elif self.receiver_id.text() == str(info_mbr_id):
            Ui_MainWindow().message_box_1(QMessageBox.Warning, '경고', '자신에게 양도할 수 없습니다.', '확인', )
        else:
            import copy
            give_start_date = self.startDateEdit.date()
            give_end_date = self.endDateEdit.date()
            rcvr_mbr_id = self.receiver_id.text()
            created_time = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
            changed_time = datetime.today().strftime('%Y-%m-%d %H:%M:%S')

            df_enroll_col = list([col for col in df_enroll])
            enroll_arr = df_enroll.values.tolist()
            enroll_arr_temp1 = []           # 양도
            enroll_arr_temp2 = []           # 양수(
            receive_end_date = ''
            for i in range(len(enroll_arr)):
                if info_mbr_id == enroll_arr[i][0] and info_enroll_counter == enroll_arr[i][1]:
                    for j in range(len(enroll_arr[i])):
                        enroll_arr_temp1.append(enroll_arr[i][j])
                    enroll_arr.__delitem__(i)
                    break
            for i in range(0, len(member_dtl_info_arr)):
                if member_dtl_info_arr[i][0] == int(self.receiver_id.text()):
                    counter = member_dtl_info_arr[i][16]
                    receive_end_date = member_dtl_info_arr[i][18]
                    break
                    
            if counter == ' ':          # 신규 회원일 때 counter 값을 가지지 못함
                counter = 0
                enroll_arr_temp2.append(int(self.receiver_id.text()))
                # 신규 회원일 경우는 record가 없기 때문에 실행 시 out_of_range라는 오류가 발생하므로 임의로 빈 값을 넣어줌
                for j in range(0,9):            # enroll_list에 있는 회원번호 이후의 column 수(9개)
                    enroll_arr_temp2.append(' ')
            else:
                for i in range(len(enroll_arr)):    # 신규 회원이 아닐 경우
                    if enroll_arr[i][0] == int(self.receiver_id.text()) and enroll_arr[i][1] == counter:
                        for j in range(len(enroll_arr[i])):
                            enroll_arr_temp2.append(enroll_arr[i][j])
                        enroll_arr.__delitem__(i)
                        break

            if enroll_arr_temp1[4] == "(재시작)":
                status_flag = "(양도),(재시작)"
                status_tag = "(" + str(days_left) + "),(" + enroll_arr_temp1[5] + ")"
            else:
                status_flag = "(양도)"
                status_tag = days_left

            enroll_arr_target_g = copy.deepcopy(enroll_arr_temp1)
            if today_QDate < info_QDate_start:
                enroll_arr_target_g[3] = enroll_arr_target_g[2]
            else:
                enroll_arr_target_g[3] = QDate.toString(today_QDate, 'yyyy-MM-dd')
            enroll_arr_target_g[4] = status_flag
            enroll_arr_target_g[5] = status_tag
            enroll_arr_target_g[8] = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
            enroll_arr_target_g[9] = global_created_by
            enroll_arr.append(enroll_arr_target_g)

            enroll_arr_target_r1 = copy.deepcopy(enroll_arr_temp2)
            if  QDate.fromString(receive_end_date, "yyyy-MM-dd") >= today_QDate:
                enroll_arr_target_r1[3] =  QDate.toString(QDate.fromString(enroll_arr_temp2[3], 'yyyy-MM-dd').addDays(days_left + 1), 'yyyy-MM-dd')
                enroll_arr_target_r1[4] = "(양수)"
                enroll_arr_target_r1[5] = "(" + str(enroll_arr_temp1[0]) + ":[" + str(enroll_arr_temp1[1]) + "], " + str(status_tag) + ")"
                enroll_arr_target_r1[8] = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
                enroll_arr_target_r1[9] = global_changed_by
                enroll_arr.append(enroll_arr_target_r1)
            else:
                if counter != 0:            # 신규 회원이 아닐 때
                    enroll_arr.append(enroll_arr_target_r1)
                enroll_arr_target_r2 = copy.deepcopy(enroll_arr_temp2)
                enroll_arr_target_r2[1] = counter + 1
                enroll_arr_target_r2[2] = self.recv_str_date.toPlainText()
                enroll_arr_target_r2[3] = self.recv_end_date.toPlainText()
                enroll_arr_target_r2[4] = "(양수)"
                enroll_arr_target_r2[5] = "(" + str(enroll_arr_temp1[0]) + ":[" + str(enroll_arr_temp1[1]) + "], " + str(days_left) + ")"
                enroll_arr_target_r2[6] = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
                enroll_arr_target_r2[7] = global_created_by
                enroll_arr_target_r2[8] = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
                enroll_arr_target_r2[9] = global_created_by
                enroll_arr.append(enroll_arr_target_r2)

            list.sort(enroll_arr, key=lambda k: (k[0], k[1]))
            df = pd.DataFrame(enroll_arr, columns=df_enroll_col)

            df_memo = pd.read_excel('table/memo.xlsx')
            df_memo_col = list([col for col in df_memo])
            df_memo_row = df_memo[df_memo['회원번호'] == int(info_mbr_id)]
            df_memo_row_list = df_memo_row.values.tolist()

            df_memo_list = df_memo.values.tolist()
            memo_content = "양수자 : " + self.receiver_id.text() + " / " + self.receiver_name.toPlainText() + \
                        "\n사유 : " + self.reasonText.text() + \
                        "\n양도 기간 : " + QDate.toString(give_start_date, 'yyyy-MM-dd') + " ~ " + \
                           QDate.toString(give_end_date, 'yyyy-MM-dd')
            df_give_arr = [int(info_mbr_id), "(시스템) 회원권 양도 내역", memo_content,
                           created_time, global_created_by, changed_time, global_changed_by]
            df_memo_list.append(df_give_arr)
            df_memo_row2 = df_memo[df_memo['회원번호'] == int(rcvr_mbr_id)]

            memo_content2 = "양도자 : " + str(info_mbr_id) + " / " + info_name + \
                           "\n사유 : " + self.reasonText.text() + \
                           "\n양수 기간 : " + self.recv_str_date.toPlainText() + " ~ " + \
                            self.recv_end_date.toPlainText()
            df_take_arr = [int(rcvr_mbr_id), "(시스템) 회원권 양수 내역", memo_content2,
                           created_time, global_created_by, changed_time, global_changed_by]
            df_memo_list.append(df_take_arr)
            list.sort(df_memo_list, key=lambda k: (k[0], k[5]))
            df_memo = pd.DataFrame(df_memo_list, columns=df_memo_col)

            Ui_MainWindow().message_box_2(QMessageBox.Question, '확인', '양도하시겠습니까?', '예', '아니오')
            if MsgBoxRtnSignal == 'Y':
                Ui_MainWindow().message_box_1(QMessageBox.NoIcon, '양도 완료', '정상 처리되었습니다.', '확인', )
                df.to_excel('table/enroll_list.xlsx', index=False)
                df_memo.to_excel('table/memo.xlsx', index=False)
                self.close()
            else:
                pass

    # Label 출력
    def retranslateUi(self):
        _translate = QCoreApplication.translate

# 일시정지 Form
class Ui_pauseDialog(QDialog):
    # Setup
    def __init__(self):
        super().__init__()
        self.get_init_data()
        self.setupUi()
    
    def get_init_data(self):
        global pause_date_start, pause_date_end, days_left, new_date_start, new_date_end
        # info_QDate_start : enroll_list 기간 시작, info_QDate_end : enroll_list 기간 종료,
        # pause_date_start : 정지 시작일(고정값 변경 불가), pause_date_end = 정지 종료일,
        # new_date_start : 재 시작일(무조건 pause_date_end의 다음날),
        # new_date_end : 재 종료일(재 시작일 + (info_QDate_end - pause_date_start))

        if today_QDate >= info_QDate_start:
            pause_date_start = today_QDate
        else:
            pause_date_start = info_QDate_start
        days_left = pause_date_start.daysTo(info_QDate_end)
        pause_date_end = info_QDate_end
        new_date_start = pause_date_end.addDays(1)                # 일시정지일 다음날
        new_date_end   = new_date_start.addDays(days_left)
        
    # 화면 레이아웃
    def setupUi(self):
        self.setFixedSize(dialog_Win_size_length, dialog_Win_size_height)  # 어떤 환경이던 Dialog 크기를 고정함

        self.setWindowFlag(Qt.WindowCloseButtonHint, False)  # Window창의 Close 버튼(x모양)를 Disable함
        self.setWindowFlag(Qt.WindowContextHelpButtonHint, False)  # Window창의 Question 버튼(?모양)를 Disable함
        self.setWindowIcon(QIcon("img/pause.png"))  # Window창의 Title옆의 Icon 모양 Setting
        self.setStyleSheet("background: white")  # Dialog의 배경색을 하얀색으로 설정
        self.setWindowTitle("회원권 일시정지")

        # Title(상세 정보)
        self.titleLabel = QLabel(self)  # QDialog에 QLabel을 선언
        self.titleLabel.setGeometry(QRect(0, 20, 400, 60))  # 위치
        self.titleLabel.setText("회원권 일시정지")
        self.titleLabel.setAlignment(Qt.AlignCenter)
        # Font 속성 //
        font = QFont()
        font.setFamily("에스코어 드림 8 Heavy")
        font.setPointSize(24)
        self.titleLabel.setFont(font)  # //
        #
        # Save, Cancel Button Setting
        self.buttonBox = QDialogButtonBox(self)  # Dialog 버튼 Setting
        self.buttonBox.setGeometry(QRect(10, 540, 345, 40))  # 위치
        self.buttonBox.setOrientation(Qt.Horizontal)  # 버튼들 수평으로 보임
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel | QDialogButtonBox.Save)  # Save, Cancel 버튼 설정
        self.buttonBox.button(QDialogButtonBox.Save).setText("확인")  # Save -> 변경
        self.buttonBox.button(QDialogButtonBox.Cancel).setText("취소")  # Cancel -> 취소
        self.buttonBox.accepted.connect(self.pauseMembership)  # 회원권 일시정지 이벤트 연결
        self.buttonBox.rejected.connect(self.reject)  # 취소 이벤트 연결

        # Layout
        self.gridLayoutWidget = QWidget(self)
        self.gridLayoutWidget.setGeometry(QRect(20, 100, 340, 280))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setSizeConstraint(QGridLayout.SetMinAndMaxSize)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(20)

        label_arr = ["회원 정보", "정지 시작일", "정지 종료일", " ", "재시작일", "   종료일"]
        for i in range(0, len(label_arr)):
            self.label = QLabel(self.gridLayoutWidget)
            font = QFont()
            font.setFamily("에스코어 드림 6 Bold")
            font.setPointSize(11)
            self.label.setFont(font)
            self.label.setText(label_arr[i])
            self.gridLayout.addWidget(self.label, i, 0, 1, 1)

        # 회원정보 Data
        self.mbrInfoValueLabel = QLabel(self.gridLayoutWidget)  # QDialog에 QLabel을 선언
        # Font 속성 //
        font = QFont()
        font.setFamily("에스코어 드림 6 Bold")
        font.setPointSize(10)
        self.mbrInfoValueLabel.setFont(font)
        self.mbrInfoValueLabel.setText(str(info_mbr_id) + " / " + str(info_name))  # 회원번호 / 이름
        self.gridLayout.addWidget(self.mbrInfoValueLabel, 0, 1, 1, 1)

        # 회원 이름 출력창
        self.memberNameText = QLabel(self)
        font = QFont()
        font.setFamily("에스코어 드림 6 Bold")
        font.setPointSize(10)
        self.memberNameText.setFont(font)
        self.memberNameText.setGeometry(QRect(220, 123, 60, 16))

        # 정지 시작일 DateEdit
        self.startDateEdit = QDateEdit(self.gridLayoutWidget)
        font = QFont()
        font.setFamily("에스코어 드림 6 Bold")
        font.setPointSize(10)
        self.startDateEdit.setFont(font)
        self.startDateEdit.setReadOnly(True)
        self.startDateEdit.setMaximumSize(QSize(16777215, 20))
        self.startDateEdit.setDate(pause_date_start)
        self.gridLayout.addWidget(self.startDateEdit, 1, 1, 1, 1)

        # 정지 종료일 DateEdit
        self.endDateEdit = QDateEdit(self.gridLayoutWidget)
        font = QFont()
        font.setFamily("에스코어 드림 6 Bold")
        font.setPointSize(10)
        self.endDateEdit.setFont(font)
        self.endDateEdit.setMaximumSize(QSize(16777215, 20))
        self.endDateEdit.setDate(pause_date_end)
        self.endDateEdit.setCalendarPopup(True)
        self.endDateEdit.dateChanged.connect(self.endDateChange)
        self.gridLayout.addWidget(self.endDateEdit, 2, 1, 1, 1)

        # 재 시작일
        self.newStartDateText = QTextEdit(self.gridLayoutWidget)
        font = QFont()
        font.setFamily("에스코어 드림 6 Bold")
        self.newStartDateText.setMaximumSize(QSize(16777215, 20))
        self.newStartDateText.setReadOnly(True)
        self.newStartDateText.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        font.setPointSize(10)
        self.newStartDateText.setFont(font)
        self.newStartDateText.setStyleSheet("border : 0")
        self.newStartDateText.setText(QDate.toString(new_date_start, 'yyyy-MM-dd'))
        self.gridLayout.addWidget(self.newStartDateText, 4, 1, 1, 1)

        # 재 종료일
        self.newEndDateText = QTextEdit(self.gridLayoutWidget)
        font = QFont()
        font.setFamily("에스코어 드림 6 Bold")
        font.setPointSize(10)
        self.newEndDateText.setReadOnly(True)
        self.newEndDateText.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.newEndDateText.setMaximumSize(QSize(16777215, 20))
        self.newEndDateText.setFont(font)
        self.newEndDateText.setStyleSheet("border : 0")
        self.newEndDateText.setText(QDate.toString(new_date_end, 'yyyy-MM-dd'))
        self.gridLayout.addWidget(self.newEndDateText, 5, 1, 1, 1)

        # 정지 사유 Label
        self.label = QLabel(self)
        self.label.setGeometry(QRect(20, 420, 80, 30))
        font = QFont()
        font.setFamily("에스코어 드림 6 Bold")
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setText("정지사유")

        # 정지사유 입력
        self.pauseReasonText = QLineEdit(self)
        self.pauseReasonText.setGeometry(QRect(30, 458, 340, 30))
        font = QFont()
        font.setFamily("에스코어 드림 4 Regular")
        font.setPointSize(10)
        self.pauseReasonText.setFont(font)

        self.retranslateUi()

    # 
    def endDateChange(self):
        pause_date_start = self.startDateEdit.date()
        pause_date_end = self.endDateEdit.date()
        days_left = pause_date_start.daysTo(info_QDate_end)

        if pause_date_start >= pause_date_end:
            self.close()
            Ui_MainWindow().message_box_1(QMessageBox.Warning, '경고', '일시정지 종료일자가 시작일자보다 빠르거나 같을 수 없습니다.', '확인')
            Ui_pauseDialog().exec_()
        elif today_QDate < info_QDate_start:
            days_left = info_QDate_start.daysTo(info_QDate_end)
            self.newStartDateText.setText(QDate.toString(pause_date_end.addDays(1), 'yyyy-MM-dd'))
            self.newEndDateText.setText(QDate.toString(pause_date_end.addDays(int(days_left) + 1), 'yyyy-MM-dd'))
        else:
            self.newStartDateText.setText(QDate.toString(pause_date_end.addDays(1), 'yyyy-MM-dd'))
            self.newEndDateText.setText(QDate.toString(pause_date_end.addDays(int(days_left) + 1), 'yyyy-MM-dd'))

    # 회원권 정지 event
    def pauseMembership(self):
        import copy
        # 기본 변수 setting
        pause_date_start = self.startDateEdit.date()
        pause_date_end = self.endDateEdit.date()
        created_time = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
        changed_time = datetime.today().strftime('%Y-%m-%d %H:%M:%S')

        df_enroll_col = list([col for col in df_enroll])
        enroll_arr = df_enroll.values.tolist()
        enroll_arr_temp1 = []

        if today_QDate < info_QDate_start:
            new_end_date = QDate.toString(pause_date_end, 'yyyy-MM-dd')
        else:
            new_end_date = QDate.toString(QDate.currentDate(), 'yyyy-MM-dd')

        for i in range(len(enroll_arr)):
            if info_mbr_id == enroll_arr[i][0] and info_enroll_counter == enroll_arr[i][1]:
                for j in range(len(enroll_arr[i])):
                    enroll_arr_temp1.append(enroll_arr[i][j])
                enroll_arr.__delitem__(i)
                break
        if enroll_arr_temp1[4] == "(양수)":
            status_flag = "(정지), (양수)"
            status_tag = "(" + str(days_left) + "), (" + enroll_arr_temp1[5] + ")"
        elif enroll_arr_temp1[4] == "(재시작)":
            status_flag = "(정지), (재시작)"
            status_tag = "(" + str(days_left) + "), (" + enroll_arr_temp1[5] + ")"
        else:
            status_flag = "(정지)"
            status_tag = days_left

        for i in range(0, 2):
            if i == 0:
                enroll_arr_target1 = copy.deepcopy(enroll_arr_temp1)
                enroll_arr_target1[3] = new_end_date
                enroll_arr_target1[4] = status_flag
                enroll_arr_target1[5] = status_tag
                enroll_arr_target1[8] = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
                enroll_arr_target1[9] = global_created_by
            else:
                enroll_arr_target2 = copy.deepcopy(enroll_arr_temp1)
                enroll_arr_target2[1] = enroll_arr_temp1[1] + 1
                enroll_arr_target2[2] = self.newStartDateText.toPlainText()
                enroll_arr_target2[3] = self.newEndDateText.toPlainText()
                enroll_arr_target2[4] = "(재시작)"
                enroll_arr_target2[5] = "(" + str(enroll_arr_temp1[0]) + ":[" + str(enroll_arr_temp1[1]) + "], " + str(days_left) + ")"
                enroll_arr_target2[6] = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
                enroll_arr_target2[7] = global_created_by
                enroll_arr_target2[8] = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
                enroll_arr_target2[9] = global_created_by
        enroll_arr.append(enroll_arr_target1)
        enroll_arr.append(enroll_arr_target2)

        df_memo = pd.read_excel('table/memo.xlsx')
        df_memo_col = list([col for col in df_memo])

        df_memo_list = df_memo.values.tolist()
        memo_content =  "사유 : " + self.pauseReasonText.text() + \
                        "\n변경 전 기간 : " + QDate.toString(info_QDate_start, 'yyyy-MM-dd') + " ~ " + \
                        QDate.toString(info_QDate_end, 'yyyy-MM-dd') + \
                        "\n변경 후 기간" + \
                        "\n   정지 기간 : " + QDate.toString(pause_date_start, 'yyyy-MM-dd') + \
                        " ~ " + QDate.toString(pause_date_end, 'yyyy-MM-dd') + \
                        "\n   재시작 기간 : " + self.newStartDateText.toPlainText() + " ~ " + self.newEndDateText.toPlainText()
        df_pause_arr = [info_mbr_id, "(시스템) 회원권 일시정지 내역", memo_content,
                       created_time, global_created_by, changed_time, global_changed_by]
        df_memo_list.append(df_pause_arr)
        list.sort(df_memo_list, key=lambda k: (k[0], k[5]))
        df_memo = pd.DataFrame(df_memo_list, columns=df_memo_col)

        list.sort(enroll_arr, key=lambda k: (k[0], k[1]))
        df = pd.DataFrame(enroll_arr, columns=df_enroll_col)

        Ui_MainWindow().message_box_2(QMessageBox.Question, '확인', '정지하시겠습니까?', '예', '아니오')
        if MsgBoxRtnSignal == 'Y':
            Ui_MainWindow().message_box_1(QMessageBox.NoIcon, '정지 완료', '정상 처리되었습니다.', '확인', )
            df.to_excel('table/enroll_list.xlsx',  index=False)
            df_memo.to_excel('table/memo.xlsx', index=False)
            self.close()
        else:
            pass

    # Label 출력
    def retranslateUi(self):
        _translate = QCoreApplication.translate

# 메모 Form
class Ui_memoDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.get_Init_Data()
        self.setupUi()

    def get_Init_Data(self):
        global get_memo_arr
        df = pd.read_excel('table/memo.xlsx', na_filter=False)
        df = df[df['회원번호'] == info_mbr_id]  # 전화번호 일치하는 행 가져오기
        get_memo_arr = df.values.tolist()[::-1]

    def setupUi(self):
        self.setFixedSize(dialog_Win_size_length, dialog_Win_size_height)  # 어떤 환경이던 Dialog 크기를 고정함

        self.setWindowFlag(Qt.WindowCloseButtonHint, False)
        self.setWindowFlag(Qt.WindowContextHelpButtonHint, False)
        self.setWindowIcon(QIcon("img/pngegg.png"))
        self.setStyleSheet("background: white")
        self.setWindowTitle("메모 리스트")

        self.titleLabel = QLabel(self)
        self.titleLabel.setGeometry(QRect(0, 20, 400, 60))
        self.titleLabel.setText("메모 리스트")
        self.titleLabel.setAlignment(Qt.AlignCenter)
        font = QFont()
        font.setFamily("에스코어 드림 8 Heavy")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.titleLabel.setFont(font)

        # 회원정보
        self.mbrInfoLabel = QLabel(self)
        self.mbrInfoLabel.setGeometry(QRect(25, 100, 220, 30))
        font = QFont()
        font.setFamily("에스코어 드림 6 Bold")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.mbrInfoLabel.setFont(font)
        self.mbrInfoLabel.setText("회원정보 : " + str(info_mbr_id) + "/" + info_name)

        button_arr = [["신규메모", "img/pencil.png", 33, 33, 340, 90, 33, 33, self.memoCreate],
                      ["나가기", "img/exit.png", 30, 55, 340, 525, 30, 40, self.close]]

        for i in range(0, len(button_arr)):
            self.pushButton = QPushButton(self)
            self.pushButton.setMaximumSize(QSize(35, 35))
            self.pushButton.setToolTip(button_arr[i][0])
            icon = QIcon()
            icon.addPixmap(QPixmap(button_arr[i][1]), QIcon.Normal, QIcon.Off)
            self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))  # Point Cursor가 손가락 Cursor로 변경
            self.pushButton.setIcon(icon)
            self.pushButton.setIconSize(QSize(button_arr[i][2], button_arr[i][3]))
            self.pushButton.setGeometry(
                 QRect(button_arr[i][4], button_arr[i][5], button_arr[i][6], button_arr[i][7]))
            self.pushButton.clicked.connect(button_arr[i][8])  # 회원가입 event 연결

        font = QFont()
        font.setFamily("에스코어 드림 8 Heavy")
        font.setPointSize(11)
        self.listWidget = QListWidget(self)
        font = QFont()
        font.setFamily("에스코어 드림 4 Regular")
        font.setPointSize(10)
        self.listWidget.setFont(font)
        self.listWidget.setGeometry(QRect(25, 130, 350, 380))
        self.listWidget.setObjectName("listWidget")
        for i in get_memo_arr[::-1]:
            item = QListWidgetItem()
            self.listWidget.addItem(item)

        self.listWidget.itemClicked.connect(self.listItemClicked)

        self.retranslateUi()

    def memoCreate(self):
        self.close()
        win = Ui_memoCreateDialog()
        win.exec_()

    def listItemClicked(self):
        global memo_idx
        global get_memo
        current_row = self.listWidget.currentRow()
        get_memo = get_memo_arr[current_row]
        memo_idx = len(get_memo_arr) - current_row
        try:
            get_memo
        except NameError:
            pass  # pass (중요) : 함수 무효화
        else:
            # 회원권 등록 Dialog 연결 (Bookmark 2)
            self.close()
            win = Ui_memoChangeDialog()
            win.exec_()

    def retranslateUi(self):
        _translate = QCoreApplication.translate
        label_arr = ["날짜", "내용"]
        df = pd.read_excel('table/memo.xlsx', na_filter=False)
        # df_col = list([col for col in df])
        df = df[df['회원번호'] == info_mbr_id]  # 전화번호 일치하는 행 가져오기
        df_list = df.values.tolist()[::-1]

        # # 테이블 안에 아무것도 없으면 오류가 뜸(j = 3일때)
        __sortingEnabled = self.listWidget.isSortingEnabled()
        # self.listWidget.setSortingEnabled(False)
        if len(df_list) != 0:
            for i in range(0, len(df_list)):
                item = self.listWidget.item(i)
                item.setText(_translate("Dialog", str(df_list[i][5]) + '        ' + str(df_list[i][1])))

        self.listWidget.setSortingEnabled(__sortingEnabled)

# 메모 생성 Form
class Ui_memoCreateDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.setFixedSize(dialog_Win_size_length, dialog_Win_size_height)  # 어떤 환경이던 Dialog 크기를 고정함

        self.setWindowFlag(Qt.WindowCloseButtonHint, False)
        self.setWindowFlag(Qt.WindowContextHelpButtonHint, False)
        self.setWindowIcon(QIcon("img/pencil.png"))
        self.setStyleSheet("background: white")
        self.setWindowTitle("신규 메모등록")

        # Title
        self.titleLabel = QLabel(self)
        self.titleLabel.setGeometry(QRect(0, 20, 400, 60))
        self.titleLabel.setText("신규 메모등록")
        self.titleLabel.setAlignment(Qt.AlignCenter)
        font = QFont()
        font.setFamily("에스코어 드림 8 Heavy")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.titleLabel.setFont(font)

        # 회원정보
        self.mbrInfoLabel = QLabel(self)
        self.mbrInfoLabel.setGeometry(QRect(25, 100, 220, 30))
        font = QFont()
        font.setFamily("에스코어 드림 6 Bold")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.mbrInfoLabel.setFont(font)
        self.mbrInfoLabel.setText("회원정보 : " + str(info_mbr_id) + "/" + info_name)

        # 생성일
        self.toDayLabel = QLabel(self)
        self.toDayLabel.setGeometry(QRect(255, 100, 105, 30))
        font = QFont()
        font.setFamily("에스코어 드림 6 Bold")
        font.setPointSize(11)
        font.setBold(True)
        self.toDayLabel.setFont(font)
        self.toDayLabel.setText(date.today().strftime('%Y-%m-%d'))

        # 제목 Label
        self.memoTitleLabel = QLabel(self)
        self.memoTitleLabel.setGeometry(QRect(25, 135, 50, 30))
        self.memoTitleLabel.setText("제목 : ")
        font = QFont()
        font.setFamily("에스코어 드림 6 Bold")
        font.setPointSize(10)
        self.memoTitleLabel.setFont(font)

        # 제목 입력
        self.memoTitleLineEdit = QLineEdit(self)
        self.memoTitleLineEdit.setGeometry(QRect(80, 135, 300, 30))
        font = QFont()
        font.setFamily("에스코어 드림 4 Regular")
        font.setPointSize(10)
        self.memoTitleLineEdit.setFont(font)

        # 메모내용 입력
        self.memoInputLineEdit = QTextEdit(self)
        self.memoInputLineEdit.setGeometry(QRect(20, 180, 360, 350))
        font = QFont()
        font.setFamily("에스코어 드림 4 Regular")
        font.setPointSize(10)
        self.memoInputLineEdit.setFont(font)

        # 저장, 나가기 Button
        self.buttonBox = QDialogButtonBox(self)
        self.buttonBox.setGeometry(QRect(10, 540, 345, 40))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel | QDialogButtonBox.Ok)
        self.buttonBox.button(QDialogButtonBox.Ok).setText("확인")
        self.buttonBox.button(QDialogButtonBox.Cancel).setText("취소")

        self.retranslateUi()

        self.buttonBox.accepted.connect(self.memoCreate)
        self.buttonBox.rejected.connect(self.memoReject)

    def memoCreate(self):
        global memo_arr

        if self.memoInputLineEdit.toPlainText() == '' or self.memoTitleLineEdit.text() == '':
            Ui_MainWindow().message_box_1(QMessageBox.Warning, '경고', '어떤 정보도 입력되지 않았습니다', '확인')
            pass
        else:
            Ui_MainWindow().message_box_2(QMessageBox.Question, '확인', '저장하시겠습니까?', '예', '아니오')
            if MsgBoxRtnSignal == 'Y':
                member_num = info_mbr_id
                memo_title = self.memoTitleLineEdit.text()
                content = self.memoInputLineEdit.toPlainText()
                created_time = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
                changed_time = datetime.today().strftime('%Y-%m-%d %H:%M:%S')

                memo_arr = [member_num, str(memo_title), str(content), created_time, global_created_by,
                            changed_time, global_changed_by]

                df = pd.read_excel('table/memo.xlsx', na_filter=False)
                df_col = list([col for col in df])
                df_list = df.values.tolist()
                df_list.append(memo_arr)
                #
                list.sort(df_list, key=lambda k: (k[0], k[5]))
                df = pd.DataFrame(df_list, columns=df_col)
                df.to_excel('table/memo.xlsx', index=False)

                Ui_MainWindow().message_box_1(QMessageBox.Information, '정보', '저장되었습니다', '확인')
                self.close()
                Ui_memoDialog().exec_()

            elif MsgBoxRtnSignal == 'N':
                pass

    def memoReject(self):
        self.close()
        Ui_memoDialog().exec_()

    def retranslateUi(self):
        _translate = QCoreApplication.translate

# 메모 변경 Form
class Ui_memoChangeDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.get_Init_Data()
        self.setupUi()

    def get_Init_Data(self):
        global change_date_arr, change_date
        change_date = get_memo[5]
        change_date_arr = change_date.split(' ')
        change_date = QDate.fromString(change_date_arr[0], 'yyyy-MM-dd')

    def setupUi(self):
        self.setFixedSize(dialog_Win_size_length, dialog_Win_size_height)  # 어떤 환경이던 Dialog 크기를 고정함

        self.setWindowFlag(Qt.WindowCloseButtonHint, False)
        self.setWindowFlag(Qt.WindowContextHelpButtonHint, False)
        self.setWindowIcon(QIcon("img/pencil.png"))
        self.setStyleSheet("background: white")

        # Title
        self.titleLabel = QLabel(self)
        self.titleLabel.setGeometry(QRect(0, 20, 400, 60))
        self.titleLabel.setAlignment(Qt.AlignCenter)
        font = QFont()
        font.setFamily("에스코어 드림 8 Heavy")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.titleLabel.setFont(font)

        # 회원정보
        self.mbrInfoLabel = QLabel(self)
        self.mbrInfoLabel.setGeometry(QRect(25, 100, 220, 30))
        font = QFont()
        font.setFamily("에스코어 드림 6 Bold")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.mbrInfoLabel.setFont(font)
        self.mbrInfoLabel.setText("회원정보 : " + str(info_mbr_id) + "/" + info_name)

        # 기 생성일
        self.createdDateLabel = QLabel(self)
        self.createdDateLabel.setGeometry(QRect(255, 100, 105, 30))
        font = QFont()
        font.setFamily("에스코어 드림 6 Bold")
        font.setPointSize(11)
        font.setBold(True)
        self.createdDateLabel.setFont(font)
        self.createdDateLabel.setText(change_date_arr[0])

        # 제목 Label
        self.memoTitleLabel = QLabel(self)
        self.memoTitleLabel.setGeometry(QRect(25, 135, 50, 30))
        self.memoTitleLabel.setText("제목 : ")
        font = QFont()
        font.setFamily("에스코어 드림 6 Bold")
        font.setPointSize(10)
        self.memoTitleLabel.setFont(font)

        # 제목 입력
        self.memoTitleLineEdit = QLineEdit(self)
        self.memoTitleLineEdit.setGeometry(QRect(80, 135, 300, 30))
        font = QFont()
        font.setFamily("에스코어 드림 4 Regular")
        font.setPointSize(10)
        self.memoTitleLineEdit.setFont(font)

        # 메모내용 입력
        self.memoInputLineEdit = QTextEdit(self)
        self.memoInputLineEdit.setGeometry(QRect(20, 180, 360, 350))
        font = QFont()
        font.setFamily("에스코어 드림 4 Regular")
        font.setPointSize(10)
        self.memoInputLineEdit.setFont(font)

        # change_date = get_memo[5]
        # change_date_arr = change_date.split(' ')
        # change_date = QDate.fromString(change_date_arr[0], 'yyyy-MM-dd')

        self.buttonBox = QDialogButtonBox(self)
        self.buttonBox.setGeometry(QRect(QRect(10, 540, 345, 40)))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setObjectName("buttonBox")

        if today_QDate > change_date or get_memo[1].split(' ')[0] == "(시스템)":
            self.memoInputLineEdit.setReadOnly(True)
            self.memoTitleLineEdit.setReadOnly(True)
            self.buttonBox.setStandardButtons(QDialogButtonBox.Ok)
            self.buttonBox.button(QDialogButtonBox.Ok).setText("확인")
            self.buttonBox.accepted.connect(self.memoChange)
        else:
            self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel | QDialogButtonBox.Ok)
            self.buttonBox.button(QDialogButtonBox.Ok).setText("확인")
            self.buttonBox.button(QDialogButtonBox.Cancel).setText("취소")
            self.buttonBox.accepted.connect(self.memoChange)
            self.buttonBox.rejected.connect(self.memoReject)

        self.retranslateUi()

    def memoChange(self):
        if self.memoInputLineEdit.toPlainText() == '' or self.memoTitleLineEdit.text() == '':
            Ui_MainWindow().message_box_1(QMessageBox.Warning, '경고', '어떤 정보도 입력되지 않았습니다', '확인')
            pass
        elif change_date < today_QDate or get_memo[1].split(' ')[0] == "(시스템)":
            self.close()
            Ui_memoDialog().exec_()
        else:
            Ui_MainWindow().message_box_2(QMessageBox.Question, '확인', '변경하시겠습니까?', '예', '아니오')
            if MsgBoxRtnSignal == 'Y':
                Ui_MainWindow().message_box_1(QMessageBox.NoIcon, '확인', '변경되었습니다.', '확인')
                member_num = get_memo[0]
                date_now = date.today().strftime('%Y-%m-%d')
                memo_title = self.memoTitleLineEdit.text()
                content = self.memoInputLineEdit.toPlainText()
                created_time = get_memo[3]
                created_by = get_memo[4]
                changed_time = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
                changed_by = 'admin'

                memo_arr = [member_num, str(memo_title), str(content), created_time, created_by,
                            changed_time, changed_by]

                df = pd.read_excel('table/memo.xlsx', na_filter=False)
                df_col = list([col for col in df])

                df_del_row = df[(df['회원번호'] == get_memo[0]) & (df['제목'] == get_memo[1]) &
                                (df['내용'] == get_memo[2]) & (df['생성일'] == created_time)]  # 전화번호 일치하는 행 가져오기
                df = df.drop(df_del_row.index)
                df_list = df.values.tolist()

                df_list.append(memo_arr)
                #
                list.sort(df_list, key=lambda k: (k[0], k[5]))
                df = pd.DataFrame(df_list, columns=df_col)
                df.to_excel('table/memo.xlsx', index=False)
                self.close()
                Ui_memoDialog().exec_()
            else:
                pass

    def memoReject(self):
        self.close()
        Ui_memoDialog().exec_()

    def retranslateUi(self):
        _translate = QCoreApplication.translate
        if today_QDate > change_date or get_memo[1].split(' ')[0] == "(시스템)":
            self.setWindowTitle(_translate("Dialog", "메모 확인"))
            self.titleLabel.setText(_translate("Dialog", "메모 확인"))
        else:
            self.setWindowTitle(_translate("Dialog", "메모 변경"))
            self.titleLabel.setText(_translate("Dialog", "메모 변경"))

        self.memoTitleLineEdit.setText(str(get_memo[1]))
        self.memoInputLineEdit.setText(str(get_memo[2]))

# 회원등록 Form
class Signup_Dialog(QDialog):
    # Setup
    def __init__(self):
        super().__init__()
        self.setupUi()

    # 회원가입 레이아웃
    def setupUi(self):
        self.setFixedSize(dialog_Win_size_length, dialog_Win_size_height)  # 어떤 환경이던 Dialog 크기를 고정함

        self.setWindowTitle("회원 등록")
        self.setWindowFlag(Qt.WindowCloseButtonHint, False)
        self.setWindowFlag(Qt.WindowContextHelpButtonHint, False)
        self.setWindowIcon(QIcon("img/user.png"))
        self.setStyleSheet("background: white")

        # Title(상세 정보)
        self.titleLabel = QLabel(self)  # QDialog에 QLabel을 선언
        self.titleLabel.setGeometry(QRect(0, 20, 400, 60))
        self.titleLabel.setText("회원 등록")
        self.titleLabel.setAlignment(Qt.AlignCenter)
        # Font 속성 //
        font = QFont()
        font.setFamily("에스코어 드림 8 Heavy")
        font.setPointSize(24)
        self.titleLabel.setFont(font)  # //

        # (*)은 필수 입력 사항입니다
        self.directionLabel = QLabel(self)  # QDialog에 QLabel을 선언
        self.directionLabel.setGeometry(QRect(10, 100, 180, 15))  # 위치
        self.directionLabel.setText("(*)은 필수 입력사항입니다.")
        # Font 속성 //
        font = QFont()
        font.setFamily("에스코어 드림 6 Bold")
        font.setPointSize(9)
        self.directionLabel.setFont(font)  # //
        # Label Text의 색깔
        palette = QPalette()
        palette.setColor(QPalette.WindowText, Qt.red)
        self.directionLabel.setPalette(palette)

        # Layout
        self.labelLayoutWidget = QWidget(self)
        self.labelLayoutWidget.setGeometry(QRect(10, 130, 82, 400))     # 위치
        self.labelLayoutWidget.setObjectName("labelLayoutWidget")

        # Layout
        self.labelBoxLayout = QVBoxLayout(self.labelLayoutWidget)
        self.labelBoxLayout.setContentsMargins(0, 0, 0, 0)
        self.labelBoxLayout.setSpacing(12)
        self.labelBoxLayout.setObjectName("labelBoxLayout")

        label_arr = ["이름    *", "생년월일    *", "성별", "이메일    *", "전화번호    *", "주소", "차량 번호", "락커 정보", "리그 등급"]

        for i in range(0, len(label_arr)):
            self.label = QLabel(self.labelLayoutWidget)  # LabelLayoutWidget에 이름 Label을 선언
            # Font 속성 //
            font = QFont()
            font.setFamily("에스코어 드림 6 Bold")
            font.setPointSize(11)
            self.label.setFont(font)  # //
            self.label.setText(label_arr[i])
            self.labelBoxLayout.addWidget(self.label)  # LabelLayout에 이름 Label을 삽입

        # Layout
        self.textLayoutWidget = QWidget(self)
        self.textLayoutWidget.setGeometry(QRect(110, 130, 261, 355))
        self.textLayoutWidget.setObjectName("textLayoutWidget")
        self.textBoxLayout = QVBoxLayout(self.textLayoutWidget)
        self.textBoxLayout.setContentsMargins(0, 4, 0, 0)
        self.textBoxLayout.setSpacing(15)
        self.textBoxLayout.setObjectName("textBoxLayout")

        # 이름 Input
        self.nameText = QLineEdit(self.textLayoutWidget)
        self.nameText.setObjectName("nameText")
        self.textBoxLayout.addWidget(self.nameText)
        font = QFont()
        font.setFamily("에스코어 드림 4 Regular")
        font.setPointSize(10)
        self.nameText.setFont(font)
        self.textBoxLayout.addWidget(self.nameText)

        # 생년월일 Input
        self.birthText = QLineEdit(self.textLayoutWidget)
        self.birthText.setObjectName("birthText")
        font = QFont()
        font.setFamily("에스코어 드림 4 Regular")
        font.setPointSize(10)
        self.birthText.setFont(font)
        self.birthText.setPlaceholderText("yyyyMMdd")
        self.textBoxLayout.addWidget(self.birthText)

        # Layout
        self.genderBoxLayout = QHBoxLayout()
        self.genderBoxLayout.setObjectName("genderBoxLayout")

        # 남자 Radio Button
        self.maleRadio = QRadioButton(self.textLayoutWidget)
        self.maleRadio.setObjectName("maleRadio")
        font = QFont()
        font.setFamily("에스코어 드림 4 Regular")
        font.setPointSize(10)
        self.maleRadio.setFont(font)
        self.maleRadio.setChecked(True)
        self.genderBoxLayout.addWidget(self.maleRadio)

        # 여자 Radio Button
        self.femaleRadio = QRadioButton(self.textLayoutWidget)
        self.femaleRadio.setObjectName("femaleRadio")
        font = QFont()
        font.setFamily("에스코어 드림 4 Regular")
        font.setPointSize(10)
        self.femaleRadio.setFont(font)
        self.genderBoxLayout.addWidget(self.femaleRadio)
        self.textBoxLayout.addLayout(self.genderBoxLayout)

        # Layout
        self.emailBoxLayout = QHBoxLayout()
        self.emailBoxLayout.setObjectName("emailBoxLayout")

        # 이메일 주소 (이름)
        self.emailAddressText = QLineEdit(self.textLayoutWidget)
        self.emailAddressText.setObjectName("emailAddressText")
        font = QFont()
        font.setFamily("에스코어 드림 4 Regular")
        font.setPointSize(10)
        self.emailAddressText.setFont(font)
        self.emailBoxLayout.addWidget(self.emailAddressText)
        # @
        self.emailConLabel = QLabel(self.textLayoutWidget)
        self.emailConLabel.setObjectName("emailConLabel")
        font = QFont()
        font.setFamily("에스코어 드림 4 Regular")
        font.setPointSize(10)
        self.emailConLabel.setFont(font)
        self.emailBoxLayout.addWidget(self.emailConLabel)
        # 이메일 주소 (Domain)
        self.emailDomainText = QLineEdit(self.textLayoutWidget)
        self.emailDomainText.setObjectName("emailDomainText")
        font = QFont()
        font.setFamily("에스코어 드림 4 Regular")
        font.setPointSize(10)
        self.emailDomainText.setFont(font)
        self.emailBoxLayout.addWidget(self.emailDomainText)

        # Layout
        self.textBoxLayout.addLayout(self.emailBoxLayout)

        # 전화번호 Input
        self.phoneNumText = QLineEdit(self.textLayoutWidget)
        self.phoneNumText.setObjectName("phoneNumText")
        font = QFont()
        font.setFamily("에스코어 드림 4 Regular")
        font.setPointSize(10)
        self.phoneNumText.setFont(font)
        self.phoneNumText.setPlaceholderText("'-' 를 포함하여 입력해주세요")
        self.textBoxLayout.addWidget(self.phoneNumText)

        # 주소 Input
        self.addressText = QLineEdit(self.textLayoutWidget)
        self.addressText.setObjectName("addressText")
        font = QFont()
        font.setFamily("에스코어 드림 4 Regular")
        font.setPointSize(10)
        self.addressText.setFont(font)
        self.textBoxLayout.addWidget(self.addressText)

        # 차량번호 Input
        self.carText = QLineEdit(self.textLayoutWidget)
        self.carText.setObjectName("carText")
        font = QFont()
        font.setFamily("에스코어 드림 4 Regular")
        font.setPointSize(10)
        self.carText.setFont(font)
        self.carText.setPlaceholderText("예시 : 12가/3456 (띄워쓰기 금지)")
        self.textBoxLayout.addWidget(self.carText)

        # 락커번호 Input
        self.lockerText = QLineEdit(self.textLayoutWidget)
        self.lockerText.setObjectName("lockerText")
        font = QFont()
        font.setFamily("에스코어 드림 4 Regular")
        font.setPointSize(10)
        self.lockerText.setFont(font)
        self.lockerText.setPlaceholderText("락커번호/락커비밀번호")
        self.textBoxLayout.addWidget(self.lockerText)

        # 리그번호 Input
        self.comboBox1 = QComboBox(self)
        self.comboBox1.setGeometry(QRect(110, 500, 60, 26))         # 위치
        self.comboBox1.setObjectName("comboBox1")
        for i in range(1, 10):
            self.comboBox1.addItem("")
        font = QFont()
        font.setFamily("에스코어 드림 6 Bold")
        font.setPointSize(10)
        self.comboBox1.setFont(font)

        # Save, Cancel Button Setting
        self.buttonBox = QDialogButtonBox(self)  # Dialog 버튼 Setting
        self.buttonBox.setGeometry(QRect(10, 540, 345, 40))  # 위치
        self.buttonBox.setOrientation(Qt.Horizontal)  # 버튼들 수평으로 보임
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel | QDialogButtonBox.Save)  # Save, Cancel 버튼 설정
        self.buttonBox.button(QDialogButtonBox.Save).setText("등록")  # Save -> 변경
        self.buttonBox.button(QDialogButtonBox.Cancel).setText("취소")  # Cancel -> 취소
        self.buttonBox.accepted.connect(self.saveMember)
        self.buttonBox.rejected.connect(self.reject)

        self.retranslateUi()

        # 성별 정보 테이블에 넣기 위한 event
        self.maleRadio.click()

    # Label 출력
    def retranslateUi(self):
        _translate = QCoreApplication.translate
        self.maleRadio.setText(_translate("Dialog", "남"))
        self.femaleRadio.setText(_translate("Dialog", "여"))
        self.emailConLabel.setText(_translate("Dialog", "@"))
        for i in range(0, 9):
            self.comboBox1.setItemText(i, _translate("Dialog", str(i + 1)))


    # 회원가입 event
    def saveMember(self):
        if self.maleRadio.isChecked():
            gender_type = '남'
        if self.femaleRadio.isChecked():
            gender_type = '여'
        phone_number = self.phoneNumText.text()
        email = self.emailAddressText.text() + '@' + self.emailDomainText.text()
        if self.lockerText.text() == '':
            locker = ['', '']
        else:
            locker = self.lockerText.text().split('/')

        if self.nameText.text() == '' or self.birthText.text() == '' or phone_number == '' or email == '@':
            Ui_MainWindow().message_box_1(QMessageBox.Warning, '경고', '필수 입력사항을 확인해주세요.', '확인')
            pass
        else:
            created_time = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
            created_by = 'admin'
            changed_time = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
            changed_by = 'admin'
            info_outp_exclude = " "
            arr = [self.nameText.text(), str(phone_number), self.birthText.text(), gender_type, email,
                   self.addressText.text(), self.carText.text(), locker[0], locker[1],
                   str(self.comboBox1.currentText()), info_outp_exclude, created_time, created_by, changed_time, changed_by]

            # member_list 엑셀파일 읽기
            df_list = df_member.values.tolist()
            df_col = list([col for col in df_member])
            arr.insert(0, df_global_list[0][20])            # 최종 회원번호 관리
            df_global_list[0][20] += 1

            df_list.append(arr)

            df = pd.DataFrame(df_list, columns=df_col)
            df_global_set = pd.DataFrame(df_global_list, columns=df_global_col)

            memo_title = "(시스템) 신규 회원 등록"
            content = created_time + "에 신규 회원 등록함."

            memo_arr = [df_global_list[0][20] - 1, str(memo_title), str(content), created_time, created_by,
                        changed_time, changed_by]

            df_memo = pd.read_excel('table/memo.xlsx')
            df_col = list([col for col in df_memo])
            df_list = df_memo.values.tolist()
            df_list.append(memo_arr)

            list.sort(df_list, key=lambda k: (k[0], k[5]))
            df_memo = pd.DataFrame(df_list, columns=df_col)

            Ui_MainWindow().message_box_2(QMessageBox.Question, '확인', '등록하시겠습니까?', '예', '아니오')
            if MsgBoxRtnSignal == 'Y':
                Ui_MainWindow().message_box_1(QMessageBox.NoIcon, '등록 완료', '등록되었습니다.', '확인', )
                df.to_excel('table/member_list.xlsx', index=False)
                df_memo.to_excel('table/memo.xlsx', index=False)
                df_global_set.to_excel('table/global_setting.xlsx', index=False)
                self.close()
            else:
                pass

# Global 환경설정
class Ui_GlobalConfig(QDialog):
    # Setup
    def __init__(self):
        super().__init__()
        self.setupUi()

    # 환경설정 레이아웃
    def setupUi(self):
        self.resize(dialog_Win_size_length, dialog_Win_size_height)
        self.setFixedSize(dialog_Win_size_length, dialog_Win_size_height)         # 어떤 환경이던 Dialog 크기를 고정함

        self.setWindowFlag(Qt.WindowCloseButtonHint, False)
        self.setWindowFlag(Qt.WindowContextHelpButtonHint, False)
        self.setWindowIcon(QIcon("img/OIP.jpg"))
        self.setStyleSheet("background: white")
        self.setWindowTitle("환경설정")

        # Title
        self.titleLabel = QLabel(self)
        self.titleLabel.setGeometry(QRect(0, 20, 400, 60))
        self.titleLabel.setText("환경 설정")
        self.titleLabel.setAlignment(Qt.AlignCenter)
        font = QFont()
        font.setFamily("에스코어 드림 8 Heavy")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.titleLabel.setFont(font)

        self.tableWidget = QTableWidget(self)
        self.tableWidget.setGeometry(QRect(20, 110, 360, 400))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        # self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tableWidget.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.tableWidget.verticalHeader().setVisible(False)

        header = self.tableWidget.horizontalHeader()
        for i in range(0, 2):
            header.setSectionResizeMode(i, QHeaderView.ResizeToContents)
            header.setStyleSheet("::section {""background-color: lightgray;""}")
            item = QTableWidgetItem()
            font = QFont()
            font.setFamily("에스코어 드림 6 Bold")
            font.setPointSize(10)
            item.setFont(font)
            self.tableWidget.setHorizontalHeaderItem(i, item)

        # 저장, 최소 Button
        self.buttonBox = QDialogButtonBox(self)
        self.buttonBox.setGeometry(QRect(10, 540, 345, 40))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel | QDialogButtonBox.Ok)
        self.buttonBox.button(QDialogButtonBox.Ok).setText("저장")
        self.buttonBox.button(QDialogButtonBox.Cancel).setText("취소")

        self.retranslateUi()
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

    def accept(self):
        df_new = df_global
        df_col = list([col for col in df_new])

        df_new = df_new.drop(index=0)
        df_list = df_new.values.tolist()
        arr = []
        for i in range(len(df_col)):
            arr.append(self.tableWidget.item(i,1).text())
        df_list.append(arr)

        list.sort(df_list, key=lambda k: k[0])
        df_new = pd.DataFrame(df_list, columns=df_col)

        Ui_MainWindow().message_box_2(QMessageBox.Question, '확인', '저장하시겠습니까?', '예', '아니오')
        if MsgBoxRtnSignal == 'Y':
            df_new.to_excel('table/global_setting.xlsx', index=False)
            Ui_MainWindow().message_box_1(QMessageBox.Information, '정보', '저장되었습니다', '확인')
            self.close()
        elif MsgBoxRtnSignal == 'N':
            pass

    def retranslateUi(self):
        _translate = QCoreApplication.translate

        header_label = ["환경 변수", "설정 값"]
        for i in range(len(header_label)):
            item = self.tableWidget.horizontalHeaderItem(i)
            item.setText(_translate("Dialog", header_label[i]))

        for i in range(0, len(df_global_col)):
            rowPosition = self.tableWidget.rowCount()
            self.tableWidget.insertRow(rowPosition)
            item = QTableWidgetItem()
            item.setTextAlignment(Qt.AlignCenter)
            item.setFlags(Qt.ItemIsEnabled)             # 특정 Cell만 read-only
            item.setBackground(QColor(255, 255, 255, 0))
            self.tableWidget.setItem(i, 0, item)
            font = QFont()
            font.setFamily("에스코어 드림 6 Bold")
            font.setPointSize(10)
            item.setFont(font)
            item.setBackground(QColor("lightgreen"))
            item = self.tableWidget.item(i, 0)
            item.setText(_translate("Dialog", str(df_global_col[i])))
            item = QTableWidgetItem()
            self.tableWidget.setItem(i, 1, item)
            font = QFont()
            font.setFamily("에스코어 드림 4 Regular")
            font.setPointSize(10)
            item.setFont(font)
            item = self.tableWidget.item(i, 1)
            item.setText(_translate("Dialog", str(df_global_list[0][i])))

# Log In Form
class Ui_LogIn_Dialog(QDialog):
    # Setup
    def __init__(self):
        super().__init__()
        self.setupUi()

    # Log In 레이아웃
    def setupUi(self):
        self.resize(340, 150)
        self.setFixedSize(340, 150)         # 어떤 환경이던 Dialog 크기를 고정함

        self.setWindowFlag(Qt.WindowCloseButtonHint, False)
        self.setWindowFlag(Qt.WindowContextHelpButtonHint, False)
        self.setWindowIcon(QIcon("img/OIP.jpg"))
        self.setStyleSheet("background: white")
        self.setWindowTitle("로그인")

        self.widget = QWidget(self)
        self.widget.setGeometry(QRect(30, 20, 280, 85))
        self.widget.setObjectName("widget")

        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")

        self.IdLabel = QLabel(self.widget)
        self.IdLabel.setText("관리자 아이디")
        self.setFont()
        self.IdLabel.setFont(font)
        self.IdLabel.setObjectName("label")
        self.gridLayout.addWidget(self.IdLabel, 0, 0, 1, 1)

        self.IdInputLineEdit = QLineEdit(self.widget)
        self.IdInputLineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.IdInputLineEdit, 0, 1, 1, 1)

        self.pwdLabel = QLabel(self.widget)
        self.pwdLabel.setText("관리자 비밀번호")
        self.setFont()
        self.pwdLabel.setFont(font)
        self.pwdLabel.setObjectName("label_3")
        self.gridLayout.addWidget(self.pwdLabel, 1, 0, 1, 1)

        self.pwdInputLineEdit = QLineEdit(self.widget)
        self.pwdInputLineEdit.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.pwdInputLineEdit, 1, 1, 1, 1)

        self.buttonBox = QDialogButtonBox(self)
        self.buttonBox.setGeometry(QRect(-46, 114, 350, 30))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.buttonBox.button(QDialogButtonBox.Ok).setText("로그인")
        self.buttonBox.button(QDialogButtonBox.Cancel).setText("취소")

        self.retranslateUi()
        self.buttonBox.accepted.connect(self.go_config)
        self.buttonBox.rejected.connect(self.reject)

    def setFont(self):
        global font
        font = QFont()
        font.setFamily("에스코어 드림 6 Bold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)

    def go_config(self):
        if self.IdInputLineEdit.text() == admin_id and self.pwdInputLineEdit.text() == admin_pwd:
            self.close()
            win = Ui_GlobalConfig()
            win.exec_()
        else:
            Ui_MainWindow().message_box_1(QMessageBox.Warning, '경고', '아이디 혹은 비밀번호가 틀렸습니다. 다시 한번 확인해주세요', '확인', )
            pass

    def retranslateUi(self):
        _translate = QCoreApplication.translate

class Ui_ChartDialog(QDialog):
    # Setup
    def __init__(self):
        super().__init__()
        self.setupUi()

    # 환경설정 레이아웃
    def setupUi(self):
        self.resize(dialog_Win_size_length, dialog_Win_size_height)
        self.setFixedSize(dialog_Win_size_length, dialog_Win_size_height)         # 어떤 환경이던 Dialog 크기를 고정함

        self.setWindowFlag(Qt.WindowCloseButtonHint, False)
        self.setWindowFlag(Qt.WindowContextHelpButtonHint, False)
        self.setWindowIcon(QIcon("img/analytics.png"))
        self.setStyleSheet("background: white")
        self.setWindowTitle("사용자 분포")

        # Title
        self.titleLabel = QLabel(self)
        self.titleLabel.setGeometry(QRect(0, 20, 400, 60))
        self.titleLabel.setText("사용자 분표")
        self.titleLabel.setAlignment(Qt.AlignCenter)
        font = QFont()
        font.setFamily("에스코어 드림 8 Heavy")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.titleLabel.setFont(font)

        button_arr = [["나가기", "img/exit.png", 30, 55, 340, 525, 30, 40, self.close]]

        for i in range(0, len(button_arr)):
            self.pushButton = QPushButton(self)
            self.pushButton.setMaximumSize(QSize(35, 35))
            self.pushButton.setToolTip(button_arr[i][0])
            icon = QIcon()
            icon.addPixmap(QPixmap(button_arr[i][1]), QIcon.Normal, QIcon.Off)
            self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))  # Point Cursor가 손가락 Cursor로 변경
            self.pushButton.setIcon(icon)
            self.pushButton.setIconSize(QSize(button_arr[i][2], button_arr[i][3]))
            self.pushButton.setGeometry(
                QRect(button_arr[i][4], button_arr[i][5], button_arr[i][6], button_arr[i][7]))
            self.pushButton.clicked.connect(button_arr[i][8])  # 회원가입 event 연결

        self.fig = plt.Figure(figsize=(3,4))
        plt.rcParams['font.family'] = 'Malgun Gothic'
        self.canvas = FigureCanvas(self.fig)
        print(matplotlib.matplotlib_fname())
        layout = QVBoxLayout(self)
        layout.addStretch(1)
        layout.addWidget(self.canvas)
        layout.addStretch(1)
        x = ["전체", "신규", "정상", "10일내", "5일내"]
        values = [len(member_color), member_color.count("blue"), member_color.count("green"),
                  member_color.count("yellow"), member_color.count("red")]
        colors = ['black', 'blue', 'green', 'yellow', 'red']

        if gray_color_excl != "x":
            x.append("정지")
            values.append(member_color.count("gray"))
            colors.append('gray')

        self.fig.clear()
        ax = self.fig.add_subplot(1,1,1)
        rects = ax.bar(x, values, color=colors)

        ax.set_xlabel("회원 유형", fontweight='bold')
        ax.set_ylabel("회원 수", fontweight='bold')
        ax.legend()

        for rect in rects:
            height = rect.get_height()
            ax.text(rect.get_x() + rect.get_width()/2., 1.00*height, '%d' % int(height), ha='center', va='bottom')
        self.canvas.draw()
        self.retranslateUi()

    def retranslateUi(self):
        _translate = QCoreApplication.translate


# 회원 리스트(메인화면)
class Ui_MainWindow(QMainWindow):
    # Setup
    def __init__(self):
        super().__init__()
        self.get_Init_Data()
        self.setupUi()

        # Table 내용 클릭 event
        self.tableWidget.cellClicked.connect(self.handleCellClicked)

    # Excel File로 부터 환경 및 리스트 출력 정보를 추출함
    def get_Init_Data(self):
        # 다른 'form'으로 정보 전달을 위한 array 선언
        global arr, member_dtl_info_arr, df_global, df_global_col, df_global_list, today_QDate
        global df_member, df_enroll, df_merge
        global member_dtl_temp_arr, member_dtl_info_arr, searched_name

        member_dtl_temp_arr = []
        today_QDate = QDate.currentDate()

        df_global = pd.read_excel('table/global_setting.xlsx')
        df_global.replace(np.NaN, ' ', inplace=True)
        df_global_col = list([col for col in df_global])
        df_global_list = df_global.values.tolist()
        searched_name = ''

        self.global_variable_setting()

        # member_list 엑셀 파일 읽기
        df_member = pd.read_excel('table/member_list.xlsx', na_filter=False)
        df_enroll = pd.read_excel('table/enroll_list.xlsx', na_filter=False)

        df_merge = pd.merge(df_member, df_enroll, on='회원번호', how='outer')
        df_merge.replace(np.NaN, ' ', inplace=True)

        if df_merge.empty == False:
            arr = df_merge.values.tolist()
            member_num_first = arr[0][0]
            member_num_last = arr[::-1][0][0]
            member_dtl_info_arr = []
            for i in range(member_num_first, member_num_last + 1):
                df_new = df_merge[df_merge['회원번호'] == i]
                if df_new.empty == True:
                    continue
                df_new = df_new.tail(1)
                df_arr = df_new.values.tolist()[0]
                end_qdate = QDate.fromString(str(df_arr[18]), 'yyyy-MM-dd')    # 회원권 종료일

                if mbr_del_excl != " " and df_arr[11] == "x":          # Global Setting의 회원삭제 출력제외 Option에서 회원이 출력제외 대상인 경우
                    continue
                if gray_color_excl != " ":
                    if df_arr[17] != " ":                       # 신규회원이 아닌 경우
                        if today_QDate.daysTo(end_qdate) <= gray_color_days:  # 회색신호등(정지)출력제외 and 신규회원 제외 and 회색신호등(일수)이 지남
                            continue
                        if df_arr[17] == df_arr[18]:            # 시작일 = 종료일(미래 회원권 양도한 회원) 혹은 신규회원
                            continue
                member_dtl_info_arr.append(df_arr)      # 회원 리스트 2차원 array에 record을 append

            self.list_cleansing_by_option(9)            # Combo Box가 아닌 최초실행 구분번호(겹치지 않는 Default 값 설정)

    # 전체 화면에서 사용될 Global 변수를 정의하고 고정값 등록
    def global_variable_setting(self):
        global gray_color_excl, gray_color_days, red_color_days, yellow_color_days, tranferable_days, pause_able_days
        global admin_id, admin_pwd, mbr_del_excl
        global padding_left, padding_top
        global month_type_arr

        global global_created_by, global_changed_by
        global fee_by_type_arr, fee_dscnt_by_type_arr, final_teen_discounted

        global dialog_Win_size_length, dialog_Win_size_height

        global_created_by = df_global_list[0][0]
        global_changed_by = df_global_list[0][0]
        admin_id = str(df_global_list[0][0])                  # Admin ID
        admin_pwd = str(df_global_list[0][1])                 # Admin password
        mbr_del_excl = df_global_list[0][2]              # NotSpace:회원삭제 대상 출력제외(회원 상세화면에 출력제외에 표시대상)
        gray_color_excl = df_global_list[0][3]           # NotSpace:회색신호등(정지) 출력제외
        gray_color_days = df_global_list[0][4]                # 회색적용 일수
        red_color_days = df_global_list[0][5]                 # 적색적용 일수
        yellow_color_days = df_global_list[0][6]              # 황색적용 일수
        tranferable_days = df_global_list[0][7]               # 양도가능 잔여 일수
        pause_able_days = df_global_list[0][8]                # 일시정지가능 잔여 일수

        padding_left = "padding-left: " + str(df_global_list[0][21]) + "px"      # 상태 Icon 위치조정(좌)
        padding_top = "padding-top: " + str(df_global_list[0][22]) + "px"        # 상태 Icon 위치조정(상)
        month_type_arr = ["1개월", "3개월", "6개월", "9개월", "12개월"]
        fee_by_type_arr = [df_global_list[0][9], df_global_list[0][10], df_global_list[0][11], df_global_list[0][12],
                           df_global_list[0][13]]       # 각각 1, 3, 6, 9, 12개월치 요금
        fee_dscnt_by_type_arr = [df_global_list[0][14], df_global_list[0][15], df_global_list[0][16],
                                 df_global_list[0][17], df_global_list[0][18]]  # 각각 1, 3, 6, 9, 12개월치 할인액

        final_teen_discounted = (100 - df_global_list[0][19]) / 100             # 청소년할인 적용 후 최종 금액 적용율

        dialog_Win_size_length = 400
        dialog_Win_size_height = 600

    # TableWidget 내 출력될 정보를 내용 및 조건에 맞게 필터링을 하거나 정비함
    def list_cleansing_by_option(self, idx):
        ## idx == 0:전체, 1:신규미등록, 2: 정상, 3:정지, 4:적색, 5:황색  (기본 구조(정지출력제외 = ' '일 경우))
        if idx != 9:                                # Combo Box에서 실행된 Index 번호
            self.tableWidget.clearContents()         # tablewidget clear
            member_dtl_temp_arr.clear()              # 기존 회원 리스트 2차원 array clear
            self.tableWidget.setRowCount(0)
        for i in range(0, len(member_dtl_info_arr)):
            start_qdate = QDate.fromString(member_dtl_info_arr[i][17], 'yyyy-MM-dd')   # 회원권 시작일
            end_qdate = QDate.fromString(member_dtl_info_arr[i][18], 'yyyy-MM-dd')   # 회원권 종료일
            if searched_name != '' and searched_name != member_dtl_info_arr[i][1]:
                continue
            if idx == 0 or idx == 9:                                # 0:전체, 9:초기실행
                member_dtl_temp_arr.append(member_dtl_info_arr[i])
            if idx == 1:                                            # 회원권 시작일 :신규 미등록
               if member_dtl_info_arr[i][17] == ' ':
                  member_dtl_temp_arr.append(member_dtl_info_arr[i])
            if idx == 2:                                           # 정상
                if member_dtl_info_arr[i][17] == ' ': #신규 미등록
                   continue
                if today_QDate.daysTo(end_qdate) <= gray_color_days:  # gray(일수)
                   continue
                if start_qdate == end_qdate:
                    continue
                if today_QDate.daysTo(end_qdate) <= red_color_days and red_color_days != 0:  # red(일수)
                   continue
                if today_QDate.daysTo(end_qdate) <= yellow_color_days and yellow_color_days != 0:  # yellow(일수)
                   continue
                member_dtl_temp_arr.append(member_dtl_info_arr[i])
            if idx == 3:                                                        # 회원권 정지, 혹은 적색 혹은 황색신호등 대상
                if member_dtl_info_arr[i][17] == ' ':                           # 회원권 시작일 :신규 미등록
                   continue
                if start_qdate == end_qdate:
                    member_dtl_temp_arr.append(member_dtl_info_arr[i])
                    continue
                if gray_color_excl == " ":  # 정지대상(회색)출력                    # idx(3)은 무조건 회색신호등
                   if today_QDate.daysTo(end_qdate) <= gray_color_days:          # gray(적용일수)
                      member_dtl_temp_arr.append(member_dtl_info_arr[i])
                else:                                                            # 정지대상(회색)출력 제외, idx(3)은 적색 혹은 황색신호등
                    if red_color_days != 0:                                      # idx(3)은 무조건 적색신호등
                        if today_QDate.daysTo(end_qdate) <= red_color_days:      # red(적용일수)
                            member_dtl_temp_arr.append(member_dtl_info_arr[i])
                        continue
                    else:                                                          # idx(3)은 무조건 황색신호등
                        if yellow_color_days != 0:                                 # 황색 신호등 대상
                           if today_QDate.daysTo(end_qdate) <= yellow_color_days:  # yellow(적용일수)
                              member_dtl_temp_arr.append(member_dtl_info_arr[i])
                           continue
            if idx == 4:                                                           # idx(4)는 적색 혹은 황색신호등
                if member_dtl_info_arr[i][17] == ' ':                              # 회원권 시작일 : 신규 미등록
                   continue
                if gray_color_excl != " ":                              # 정지대상(회색)출력 제외 idx(3)은 적색신호등이 됨
                    if yellow_color_days != 0:                                  # idx(4)는 황색 신호등 대상
                        if today_QDate.daysTo(end_qdate) <= red_color_days:     # red(적용일수) 재외
                            continue
                        if today_QDate.daysTo(end_qdate) <= yellow_color_days:  # yellow(적용일수)
                            member_dtl_temp_arr.append(member_dtl_info_arr[i])
                        continue
                else:                                                  # 정지대상(회색)출력안함  회색신호등은 idx(3)고정
                    if today_QDate.daysTo(end_qdate) <= gray_color_days:  # gray(적용일수)
                        continue
                    if red_color_days != 0:  # idx(4)는 적색신호등 적용대상
                        if today_QDate.daysTo(end_qdate) <= red_color_days:  # red(적용일수)
                            member_dtl_temp_arr.append(member_dtl_info_arr[i])
                        continue
                    else:  # idx(4)는 황색신호등 적용대상
                        if yellow_color_days != 0:  # 황색 신호등 대상
                            if today_QDate.daysTo(end_qdate) <= yellow_color_days:  # yellow(적용일수)
                                member_dtl_temp_arr.append(member_dtl_info_arr[i])
                            continue
            if idx == 5:                # 무조건 황색 신호등 대상, 회색, 적색신호등 모두 살아있어야 idx(5)이 황색신호등이 될 수 있음
                if member_dtl_info_arr[i][17] == ' ':                            # 신규 미등록
                   continue
                if today_QDate.daysTo(end_qdate) <= yellow_color_days and yellow_color_days != 0:  # yellow(적용일수)
                    if today_QDate.daysTo(end_qdate) <= red_color_days:                            # gray, red(적용일수) 재외(왜냐하면 빨강일수는 회색일수보다 항상크다)
                        continue
                    member_dtl_temp_arr.append(member_dtl_info_arr[i])

        if idx != 9:    # 초기실행이 아니고 Combo Box값 선택인 경우
           self.retranslateUi()

    # 화면 레이아웃 구성
    def setupUi(self):
        global combo_list_arr, idx
        self.setObjectName("MainWindow")
        self.resize(485, 670)
        self.setMinimumSize(QSize(485, 670))
        self.setMaximumSize(485, 670)

        self.setWindowFlag(Qt.WindowCloseButtonHint, False)
        self.setWindowFlag(Qt.WindowMaximizeButtonHint, False)
        self.setWindowIcon(QIcon("img/address.png"))
        self.setStyleSheet("background: white")
        self.setWindowTitle("회원 리스트")

        self.centralwidget = QWidget()
        self.centralwidget.setObjectName("centralwidget")

        # 회원 리스트(제목)
        self.titleLabel = QLabel(self.centralwidget)
        self.titleLabel.setGeometry(QRect(0, 40, 485, 60))
        self.titleLabel.setText("회원리스트")
        self.titleLabel.setAlignment(Qt.AlignHCenter)
        font = QFont()
        font.setFamily("에스코어 드림 8 Heavy")
        font.setPointSize(28)
        self.titleLabel.setFont(font)

        self.nameLabel = QLabel(self.centralwidget)
        self.nameLabel.setGeometry(QRect(300, 173, 50, 30))
        self.nameLabel.setText("이름 : ")
        self.nameLabel.setAlignment(Qt.AlignHCenter)
        font = QFont()
        font.setFamily("에스코어 드림 8 Heavy")
        font.setPointSize(10)
        self.nameLabel.setFont(font)

        self.nameText = QLineEdit(self.centralwidget)
        self.nameText.setGeometry(QRect(350, 170, 80, 25))
        font = QFont()
        font.setFamily("에스코어 드림 4 Regular")
        font.setPointSize(10)
        self.nameText.setFont(font)
        self.nameText.setPlaceholderText("이름")

        # Table 생성
        self.tableWidget = QTableWidget(self.centralwidget)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)          # 전체 cell read-only
        self.tableWidget.setStyleSheet("gridline-color: #e1e1d0")
        self.tableWidget.setStyleSheet("setTextAlignment: AlignCenter")
        # self.tableWidget.setShowGrid(False)
        self.tableWidget.setGeometry(QRect(19, 200, 450, 400))
        self.tableWidget.setMaximumSize(QSize(450, 400))
        self.tableWidget.setMinimumSize(QSize(450, 400))
        font = QFont()
        font.setFamily("에스코어 드림 5 Medium")
        font.setPointSize(10)
        self.tableWidget.setFont(font)
        self.tableWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tableWidget.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(7)
        self.tableWidget.verticalHeader().setVisible(False)                         # index 안보이는 기능

        # Table Header 생성
        header = self.tableWidget.horizontalHeader()
        for i in range(0,7):
            header.setSectionResizeMode(i, QHeaderView.ResizeToContents)
            header.setStyleSheet("::section {""background-color: lightgray;""}")
            item = QTableWidgetItem()
            font = QFont()
            font.setFamily("에스코어 드림 6 Bold")
            font.setPointSize(10)
            item.setFont(font)
            self.tableWidget.setHorizontalHeaderItem(i, item)

        # Layout
        self.buttonLayoutWidget = QWidget(self.centralwidget)
        self.buttonLayoutWidget.setGeometry(QRect(20, 120, 351, 45))
        self.buttonLayoutWidget.setObjectName("buttonLayoutWidget")
        self.buttonBoxLayout = QHBoxLayout(self.buttonLayoutWidget)
        self.buttonBoxLayout.setContentsMargins(0, 0, 0, 0)
        self.buttonBoxLayout.setObjectName("buttonBoxLayout")

        button_arr = [["상세정보", "img/memo.png", self.detailInfo],
                      ["회원권 등록", "img/submit.png", self.enrollInfo],
                      ["회원권 양도", "img/give-money.png", self.transferInfo],
                      ["일시정지", "img/pause.png", self.pauseInfo],
                      ["메모리스트", "img/pngegg.png", self.memoInfo]]

        for i in range(0, len(button_arr)):
            self.pushButton = QPushButton(self.buttonLayoutWidget)
            self.pushButton.setMaximumSize(QSize(35, 35))
            self.pushButton.setToolTip(button_arr[i][0])
            icon = QIcon()
            icon.addPixmap(QPixmap(button_arr[i][1]), QIcon.Normal, QIcon.Off)
            self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))  # Point Cursor가 손가락 Cursor로 변경
            self.pushButton.setIcon(icon)
            self.pushButton.setIconSize(QSize(35, 35))
            self.pushButton.clicked.connect(button_arr[i][2])          # Button 클릭 시 특정 Event 발생
            self.buttonBoxLayout.addWidget(self.pushButton)

        # 리스트 필터링을 위한 Combo box
        self.signalComboBox = QComboBox(self.centralwidget)
        self.signalComboBox.setGeometry(QRect(30, 170, 94, 24))
        self.signalComboBox.setObjectName("comboBox")

        combo_list_arr = [["img/combo_ball.png", "전체"], ["img/blue_ball.png", "신규미등록"],
                          ["img/green_ball.png", "정상"], ["img/gray_ball.png", "정지"],
                          ["img/red_ball.png", str(red_color_days)+"일내"],
                          ["img/yellow_ball.png", str(yellow_color_days)+"일내"]]

        gray_idx = 0
        if gray_color_excl != " ":                        # 회색신호등(정지) 출력제외
            combo_list_arr.__delitem__(3)
            gray_idx = 1

        red_idx = 4 - gray_idx
        yellow_idx = 5 - gray_idx
        for i in range(0, len(combo_list_arr)):
            if i == red_idx and red_color_days  == 0 :     # 적색신호일수가 0일때
               continue
            if i == yellow_idx and yellow_color_days == 0 :    # 황색신호일수가 0일때
               continue
            icon = QIcon()
            icon.addPixmap(QPixmap(combo_list_arr[i][0]), QIcon.Normal, QIcon.Off)
            font = QFont()
            font.setFamily("에스코어 드림 6 Bold")
            font.setPointSize(10)
            self.signalComboBox.setFont(font)
            self.signalComboBox.addItem(icon, "")
            self.signalComboBox.setItemText(i, combo_list_arr[i][1])
        self.signalComboBox.currentIndexChanged[int].connect(self.list_cleansing_by_option)     # [int]는 combobox의 list_cleansing_by_option의 파라미터 idx 연동

        button_arr2 = [["회원등록", "img/user.png", 33, 33, 410, 120, 33, 33, self.signupInfo],
                      ["환경설정", "img/OIP.jpg", 27, 27, 420, 15, 27, 27, self.logInInfo],
                      ["최신정보 갱신", "img/refresh.png", 27, 27, 30, 15, 27, 27, self.refreshInfo],
                      ["나가기", "img/exit.png", 30, 55, 420, 610, 30, 55, self.close],
                      ["차트 조회", "img/analytics.png", 30, 30, 25, 610, 30, 30, self.showChart],
                      ["검색", "img/magnifying-glass.png", 25, 25, 440, 170, 25, 25, self.findName]]

        for i in range(0, len(button_arr2)):
            self.pushButton = QPushButton(self.centralwidget)
            self.pushButton.setMaximumSize(QSize(35, 35))
            self.pushButton.setToolTip(button_arr2[i][0])
            icon = QIcon()
            icon.addPixmap(QPixmap(button_arr2[i][1]), QIcon.Normal, QIcon.Off)
            self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))  # Point Cursor가 손가락 Cursor로 변경
            self.pushButton.setIcon(icon)
            self.pushButton.setIconSize(QSize(button_arr2[i][2], button_arr2[i][3]))
            self.pushButton.setGeometry(QRect(button_arr2[i][4], button_arr2[i][5], button_arr2[i][6], button_arr2[i][7]))
            self.pushButton.clicked.connect(button_arr2[i][8])  # 회원가입 event 연결

        self.setCentralWidget(self.centralwidget)

        self.retranslateUi()

    # 회원리스트 Header Label 출력
    def retranslateUi(self):
        _translate = QCoreApplication.translate

        table_header_label_arr = ["상태", "회원번호", "이름", "전화번호", "시작일", "종료일", "차량 번호"]
        # Header Label Display
        for i in range(len(table_header_label_arr)):
            item = self.tableWidget.horizontalHeaderItem(i)
            item.setText(_translate("MainWindow", table_header_label_arr[i]))

        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(True)
        ## TableWidget에 리스트 출력시 Sorting에 대한 기능
        #1. 먼저 Sorting 기능을 활성화 하기 위해서는 반드시 앞서 "self.tableWidget.setSortingEnabled(True)"가 지정되어야 함
        #2. self.tableWidget.sortByColumn(col_no, option)을 지정하면 TableWidget에 리스트 출력시 지정된 특정 Column을 기준으로 Sorting되어 출력됨
        #   (col_no는 헤더의 Column 순서번호, option은 [Qt.AscendingOrder, Qt.AscendingOrder]중 하나 선택됨
        #3. 특정 헤더의 Column(A Column)을 눌렀을 때 눌러진 해당 Column이 아닌 다른 Column(B Column)이 지정된 방식으로만 Sorting 되도록 하기위해서는
        #   self.tableWidget.horizontalHeader().sortIndicatorChanged.connect(self.handleSortIndicatorChanged)
        #   def handleSortIndicatorChanged(self, index, order):         # --> index: 눌러진 Column(A Column), order: 0(Ascending), 1(Descending)
        #       if index == col_no_a:                                     # --> col_no_a = (눌러진 Column(A Column))
        #          self.tableWidget.horizontalHeader().setSortIndicator(col_no_b, Qt.AscendingOrder)  # --> col_no_b(Sorting 대상 Column)

        self.append_data_to_list()

    # TableWidget에 정보 Record 추가하기
    def append_data_to_list(self):
        _translate = QCoreApplication.translate
        # 테이블 안에 아무것도 없으면 오류가 뜸(j = 3일때)
        if len(member_dtl_temp_arr) == 0:
            return

        global member_color
        member_color = []

        for i in range(0,len(member_dtl_temp_arr)):
            start_QDate = QDate.fromString(member_dtl_temp_arr[i][17], 'yyyy-MM-dd')    # 회원권 시작일
            end_QDate = QDate.fromString(member_dtl_temp_arr[i][18], 'yyyy-MM-dd')      # 회원권 종요일

            rowPosition = self.tableWidget.rowCount()
            self.tableWidget.insertRow(rowPosition)
            set_bg_clr = ''



            for j in range(0,4):                       # j: 0(상태신호등), 1(회원번호), 2(이름), 3(전화번호)
                item = QTableWidgetItem()
                if j == 0:                             # 상태 신호등
                    lbl_img = QLabel()
                    lbl_img.setScaledContents(True)
                    lbl_img.setMaximumSize(28,28)
                    if   member_dtl_temp_arr[i][17] == ' ':                                             # 회원권 시작일
                        pixmap = QPixmap('img/blue_ball.png')
                        member_color.append("blue")
                    elif today_QDate.daysTo(end_QDate) <= gray_color_days or start_QDate.daysTo(end_QDate) == 0:    # gray(적용일수)
                        pixmap = QPixmap('img/gray_ball.png')
                        member_color.append("gray")
                    elif today_QDate.daysTo(end_QDate) <= red_color_days and red_color_days != 0:       # red(적용일수)
                        pixmap = QPixmap('img/red_ball.png')
                        member_color.append("red")
                    elif today_QDate.daysTo(end_QDate) <= yellow_color_days and yellow_color_days != 0: # yellow(적용일수)
                        pixmap = QPixmap('img/yellow_ball.png')
                        member_color.append("yellow")
                    else:
                        pixmap = QPixmap('img/green_ball.png')
                        member_color.append("green")
                        if today_QDate < start_QDate:
                            set_bg_clr = 'x'
                    pixmap.scaled(QSize(15,15))
                    lbl_img.setPixmap(pixmap)
                    lbl_img.setAlignment(Qt.AlignCenter)

                    loc_adjust = "QTableWidget::item { " + padding_left + "; " + padding_top + " }"
                    self.tableWidget.setStyleSheet(loc_adjust)
                    self.tableWidget.setCellWidget(i,j,lbl_img)
                    continue

                item.setTextAlignment(Qt.AlignCenter)
                self.tableWidget.setItem(i, j, item)
                if set_bg_clr == 'x':
                    item.setBackground(QColor("lightyellow"))
                item = self.tableWidget.item(i, j)
                item.setText(_translate("MainWindow", str(member_dtl_temp_arr[i][j-1])))

            for k in range(17,19):                     # k: 17(시작일), 18(종료일)
                item = QTableWidgetItem()
                self.tableWidget.setItem(i, k-13, item)
                item = self.tableWidget.item(i, k-13)

                item.setTextAlignment(Qt.AlignCenter)
                item.setText(_translate("MainWindow", member_dtl_temp_arr[i][k]))

            item = QTableWidgetItem()
            self.tableWidget.setItem(i, 6, item)
            item = self.tableWidget.item(i, 6)
            if member_dtl_temp_arr[i][7] == '':         # 차량번호
                car_num = ''
            else:
                car_num = member_dtl_temp_arr[i][7].split('/')[1]   # 차량 뒤 네자리 번호
            item.setTextAlignment(Qt.AlignCenter)
            item.setText(_translate("MainWindow", car_num))

    # 상세정보 event
    def detailInfo(self):
        try:
            info, member_dtl_info_arr
        except NameError:
            Ui_MainWindow().message_box_1(QMessageBox.Warning, '경고', '먼저 회원을 선택하세요.', '확인')
            pass      # pass (중요) : 함수 무효화
        else:
            # 상세정보 Dialog 연결 (Bookmark 1)
            win = Ui_detailDialog()
            win.exec_()

        #TXT 형식 쓸때
        # sys.stdout = open('info.txt', 'w')
         # sys.stdout.close()
        # os.system('python detail_form.py')

    # 회원권 등록 event
    def enrollInfo(self):
        try:
            info
        except NameError:
            Ui_MainWindow().message_box_1(QMessageBox.Warning, '경고', '먼저 회원을 선택하세요.', '확인')
            pass      # pass (중요) : 함수 무효화
        else:
            # 회원권 등록 Dialog 연결 (Bookmark 2)
            win = Ui_enrollDialog()
            win.exec_()

    # 회원권 양도 event
    def transferInfo(self):
        try:
            info
        except NameError:
            Ui_MainWindow().message_box_1(QMessageBox.Warning, '경고', '먼저 회원을 선택하세요.', '확인')
            pass      # pass (중요) : 함수 무효화
        else:
            # 회원권 등록 Dialog 연결 (Bookmark 2)
            if info_start_date == ' ' and info_start_date == ' ':       # 신규회원 여부 체크
                Ui_MainWindow().message_box_1(QMessageBox.Warning, '경고', '양도 가능한 대상이 아닙니다.', '확인' )
            elif today_QDate.daysTo(info_QDate_end) <= tranferable_days:      # 양도가능 잔여일수와 비교
                Ui_MainWindow().message_box_1(QMessageBox.Warning, '경고', '양도가능 잔여일수가 충분하지 않습니다.', '확인')
            elif info_status_flag == '(양수)':
                Ui_MainWindow().message_box_1(QMessageBox.Warning, '경고', '이미 양수받은 일자를 다시 양도할 수 없습니다.', '확인')
            else:
                win = Ui_transferDialog()
                win.exec_()

    # 회원권 일시정지 event
    def pauseInfo(self):
        try:
            info
        except NameError:
            Ui_MainWindow().message_box_1(QMessageBox.Warning, '경고', '먼저 회원을 선택하세요.', '확인')
            pass      # pass (중요) : 함수 무효화
        else:
            if   today_QDate > info_QDate_end:
                Ui_MainWindow().message_box_1(QMessageBox.Warning, '경고', '일시정지 대상이 아닙니다.', '확인', )
            elif today_QDate.daysTo(info_QDate_end) <= pause_able_days:  # 일시정지 가능 잔여일수와 비교
                Ui_MainWindow().message_box_1(QMessageBox.Warning, '경고', '일시정지 가능 잔여일수가 충분하지 않습니다.', '확인')
            else:
                win = Ui_pauseDialog()
                win.exec_()

        #TXT 형식 쓸때
        # sys.stdout = open('info.txt', 'w')
        # sys.stdout.close()
        # os.system('python detail_form.py')

    # 회원권 등록 event
    def memoInfo(self):
        try:
            info
        except NameError:
            Ui_MainWindow().message_box_1(QMessageBox.Warning, '경고', '먼저 회원을 선택하세요.', '확인')
            pass  # pass (중요) : 함수 무효화
        else:
            # 회원권 등록 Dialog 연결 (Bookmark 2)
            win = Ui_memoDialog()
            win.exec_()

    # 회원가입 event
    def signupInfo(self):
        win = Signup_Dialog()               # 회원가입 Dialog 연결 (Bookmark 3)
        win.exec_()

    # 환경설정 Log In event
    def logInInfo(self):
        win = Ui_LogIn_Dialog()             # Log In Dialog 연결
        win.exec_()

    # 최신정보 갱신 event
    def refreshInfo(self):
        self.close()
        self.__init__()
        self.show()

    def findName(self):
        global searched_name
        searched_name = self.nameText.text()

        self.list_cleansing_by_option(self.signalComboBox.currentIndex())

    def showChart(self):
        win = Ui_ChartDialog()  # 회원가입 Dialog 연결 (Bookmark 3)
        win.exec_()

            # 테이블에 정비된 정보가 출력된 후 특정 Cell 클릭후 발생하는 event
    def handleCellClicked(self, row):
        global info, info_mbr_id, info_name, info_birth_date, info_phone_no, info_addr, info_car_no, \
               info_sex, info_email, info_created_on, info_created_by, info_start_date, info_end_date, \
               info_QDate_start, info_QDate_end, info_enroll_counter, info_status_flag, info_outp_exclude

        # tablewidget의 row의 회원정보와 'member_list' 엑셀 파일의 회원정보가 일치하는지 테스트
        for i in range(len(member_dtl_temp_arr)):
            if  member_dtl_temp_arr[i][0] == int(self.tableWidget.item(row, 1).text()):     # item.text는 str 속성이기 때문에 int type으로 변환해야 함
                info = member_dtl_temp_arr[i]     # 회원정보와 회원권정보가 join된 record

        if info == " ":
            return

        info_mbr_id = info[0]           # 회원번호
        info_name = info[1]             # 이름
        info_phone_no = info[2]         # 주소
        info_birth_date = info[3]       # 생년월일
        info_sex = info[4]              # 성별
        info_email = info[5]            # email 주소
        info_addr = info[6]             # 주소
        info_car_no = info[7]           # 차량번호
        info_created_on = info[12]      # 생성일
        info_created_by = info[13]      # 생성인
        info_enroll_counter = info[16]  # 회원권의 최근 순서(Index)
        info_start_date = info[17]      # 회원권시작일
        info_end_date = info[18]        # 회원권종료일
        info_status_flag = info[19]     # 회원권 상태 구분(양수, 재시작)

        if info[11] != "x":             # 출력제외
            info_outp_exclude = 0       # 출력제외: No
        else:
            info_outp_exclude = 1       # 출력제외: Yes

        info_QDate_start = QDate.fromString(info_start_date, "yyyy-MM-dd")   # 일수 연산가능 일자로 변환
        info_QDate_end = QDate.fromString(info_end_date, "yyyy-MM-dd")       # 일수 연산가능 일자로 변환

    # Message Icon Option : QMessageBox.[NoIcon, Question, Information, Warning, Critical]
    # 범용 Message Box(Single Buttons)
    def message_box_1(self, MsgOption, title, MsgText, YesText):
        msgBox1 = QMessageBox()
        msgBox1.setIcon(MsgOption)
        msgBox1.setWindowTitle(title)
        msgBox1.setText(MsgText)
        msgBox1.setStandardButtons(QMessageBox.Yes)
        buttonY = msgBox1.button(QMessageBox.Yes)
        buttonY.setText(YesText)
        msgBox1.exec_()

    # 범용 Message Box(2 Buttons)
    def message_box_2(self, MsgOption, title, MsgText, YesText, NoText):
        global MsgBoxRtnSignal

        msgBox2 = QMessageBox()
        msgBox2.setIcon(MsgOption)
        msgBox2.setWindowTitle(title)
        msgBox2.setText(MsgText)
        msgBox2.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        buttonY = msgBox2.button(QMessageBox.Yes)
        buttonY.setText(YesText)
        buttonN = msgBox2.button(QMessageBox.No)
        buttonN.setText(NoText)
        msgBox2.exec_()

        if msgBox2.clickedButton() == buttonY:
           MsgBoxRtnSignal = 'Y'
        elif msgBox2.clickedButton() == buttonN:
           MsgBoxRtnSignal = 'N'
        return MsgBoxRtnSignal

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    ui = Ui_MainWindow()
    ui.show()
    app.exec_()

## TXT 파일로 열 때 get_init_data
# with open('member_list.txt') as fp:
#     line = fp.readline()
#     line = fp.readline()
#     arr = []
#     while line:
#         arr.append(line.split("|"))
#         line = fp.readline()
# TXT 형식 쓸 때 handleCellClicked
# global get_info
# get_info = info[0] + "|" + info[1] + "|" + info[2] + "|" + info[3] + "|" + info[4] + "|" + info[5] + "|" + \
#              info[6] + "|" + info[7] + "|" + info[8] + "|" + info[9] + "|"

### 회원등록
# TXT 파일로 넣을 때
# content = self.nameText.toPlainText() + '|' + self.birthText.toPlainText() + '|' + gender_type + '|' + email \
#            + '|' + self.phoneNumText.toPlainText() + '|' + self.addressText.toPlainText() \
#           + '|' + self.carText.toPlainText() + '|' + self.lockerText.toPlainText() + '|' + self.lockerPwText.toPlainText() \
#           + '|' + self.leagueText.toPlainText() + '|
# sys.stdout = open('member_list.txt', 'a')
# sys.stdout.close()