from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

# Koordinat x dan y untuk posisi kotak
pos_x = 0
pos_y = 0

# Warna Kotak
merah = 0
hijau = 0
biru = 0


def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    gluOrtho2D(-500.0, 500.0, -500.0, 500.0)

# Membuat bentuk kotak
def kotak():
    global pos_x, pos_y
    glColor3f(merah,hijau,biru)
    
    glBegin(GL_POLYGON)
    # Kiri Atas
    glVertex2f(-50 + pos_x,-50 + pos_y)
    # Kanan Atas
    glVertex2f(50 + pos_x,-50 + pos_y)
    # Kanan Bawah
    glVertex2f(50 + pos_x,50 + pos_y)
    # Kiri Bawah
    glVertex2f(-50 + pos_x,50 + pos_y)
    glEnd()


def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.,1.0,1.0) 
    glBegin(GL_LINES)
    glVertex2f(-500.0, 0.0)
    glVertex2f(500.0, 0.0)
    glVertex2f(0.0, 500.0)
    glVertex2f(0.0, -500.0)
    glEnd()

    glPushMatrix()
    kotak()
    glPopMatrix()


    glFlush()

def input_mouse(button, state, x, y):
    global merah, hijau, biru
    # Saat mengklik kanan warna kotak akan berubah menjadi warna hijau dan biru
    if button == GLUT_RIGHT_BUTTON and state == GLUT_DOWN:
        if hijau < 1:
            merah = 0
            hijau = 1
            biru = 0
        elif biru < 1:
            merah = 0
            hijau = 0
            biru = 1
        print("Klik Kanan ditekan ", "(", x, ",", y, ")")
     # Saat mengklik kiri warna kotak akan berubah menjadi warna merah dan hitam
    elif button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        if merah < 1:
            merah = 1
            hijau = 0
            biru = 0
        else:
            merah = 0
            hijau = 0
            biru = 0
        print("Klik Kiri ditekan ", "(", x, ",", y, ")")

def input_keyboard(key,x,y):
    global pos_x, pos_y

    # Untuk mengubah posisi kotak

    if key == GLUT_KEY_UP:
        pos_y += 5
        print("Tombol Atas ditekan ", "x : ", pos_x, " y : ", pos_y)
    elif key == GLUT_KEY_DOWN:
        pos_y -= 5
        print("Tombol Bawah ditekan ", "x : ", pos_x, " y : ", pos_y)
    elif key == GLUT_KEY_RIGHT:
        pos_x += 5
        print("Tombol Kanan ditekan ", "x : ", pos_x, " y : ", pos_y)
    elif key == GLUT_KEY_LEFT:
        pos_x -= 5
        print("Tombol Kiri ditekan ", "x : ", pos_x, " y : ", pos_y)

    # Untuk Mengubah Warna backgorund window
    
    # Background Kiri Atas berubah warna menjadi Merah
    if pos_x < 0 and pos_y > 0:
        glClearColor(1.0, 0.0, 0.0, 1.0)
    # Background Kanan Atas berubah warna menjadi Hijau
    if pos_x > 0 and pos_y > 0:
        glClearColor(0.0, 1.0, 0.0, 1.0)
    # Background Kanan Bawah berubah warna menjadi Biru
    if pos_x > 0 and pos_y < 0:
        glClearColor(0.0,0.0,1.0,1.0)
    # Background Kiri Bawah berubah warna menjadi Hitam
    if pos_x < 0 and pos_y < 0:
        glClearColor(0.0,0.0,0.0,1.0)

    

def update(value):
    glutPostRedisplay()
    glutTimerFunc(10,update,0)

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
    glutInitWindowSize(500,500)
    glutInitWindowPosition(100,100)
    glutCreateWindow("Event handling Mouse & Keyboard")
    glutDisplayFunc(display)

    glutSpecialFunc(input_keyboard)
    glutMouseFunc(input_mouse)

    glutTimerFunc(50, update, 0)

    

    init()
    glutMainLoop()
    
main()