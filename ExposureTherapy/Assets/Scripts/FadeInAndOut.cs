using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class FadeInAndOut : MonoBehaviour
{
    Canvas canvas;
    Image image;
    public Canvas proceed;
    GameController gameController;

    bool fadingOut = false;
    float targetOpacity = 0f;

    public float fadeSpeed = 0.1f;

    bool timerRunning = false;

    public float mainTargetTime = 2f;
    float targetTime = 2f;

    // Start is called before the first frame update
    void Start()
    {
        canvas = GetComponent<Canvas>();
        image = transform.GetChild(0).GetComponent<Image>();
        gameController = FindObjectOfType<GameController>();
    }

    private void Update()
    {
        if (canvas.enabled && !fadingOut && gameController.GetCurrentLevel() == 1)
        {
            if (Input.GetKeyDown(KeyCode.Return))
            {
                targetOpacity = 1f;
            }
        }

        if (canvas.enabled && gameController.GetCurrentLevel() != 1 && !fadingOut)
        {
            targetOpacity = 1f;
        }

        if (timerRunning)
        {
            targetTime -= Time.deltaTime;

            if (targetTime <= 0.0f)
            {
                TimerEnded();
            }
        }
    }

    // Update is called once per frame
    void FixedUpdate()
    {
        float currentOpacity = image.color.a;

        if (currentOpacity < targetOpacity)
        {
            image.color = new Color(image.color.r, image.color.g, image.color.b, image.color.a + fadeSpeed);
            if (image.color.a > targetOpacity)
            {
                image.color = new Color(image.color.r, image.color.g, image.color.b, targetOpacity);
            }
        } 
        else if (currentOpacity > targetOpacity)
        {
            image.color = new Color(image.color.r, image.color.g, image.color.b, image.color.a - fadeSpeed);
            if (image.color.a < targetOpacity)
            {
                image.color = new Color(image.color.r, image.color.g, image.color.b, targetOpacity);
            }
        }

        if (currentOpacity == 1f && !fadingOut)
        {
            StartTimer();
        }

        if (fadingOut == true && currentOpacity == 0f)
        {
            Debug.Log("Faded back in");
            fadingOut = false;
            canvas.enabled = false;
        }
    }

    public void StartTimer()
    {
        Debug.Log("Screen completley black");
        targetTime = mainTargetTime;
        timerRunning = true;
        fadingOut = true;
        proceed.enabled = false;
        if (gameController.GetCurrentLevel() == 2 || gameController.GetCurrentLevel() == 3)
        {
            GetComponent<AudioSource>().Play();
        }
        gameController.NextLevel();
    }

    void TimerEnded()
    {
        timerRunning = false;
        targetOpacity = 0f;
    }
}
