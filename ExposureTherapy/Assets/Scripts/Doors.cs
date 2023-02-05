using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Doors : MonoBehaviour
{
    GameObject leftDoor;
    GameObject rightDoor;

    public float maximumOpening;
    public float openSpeed;

    float openDistance;
    bool isOppening;

    AudioSource audioSource;
    public AudioClip doorsOpen;
    public AudioClip doorsClose;

    void Awake()
    {
        isOppening = false;
        openDistance = 0;
    }

    // Start is called before the first frame update
    void Start()
    {
        leftDoor = transform.GetChild(0).gameObject;
        rightDoor = transform.GetChild(1).gameObject;
        audioSource = GetComponent<AudioSource>();
    }

    // Update is called once per frame
    void Update()
    {
        if (isOppening)
        { 
            if (openDistance < maximumOpening)
            {
                float move = openSpeed * Time.deltaTime;
                openDistance += move;
                leftDoor.transform.Translate(-move, 0f, 0f);
                rightDoor.transform.Translate(move, 0f, 0f);
            }
        }
        else
        {
            if (openDistance > 0)
            {
                float move = openSpeed * Time.deltaTime;
                openDistance -= move;
                leftDoor.transform.Translate(move, 0f, 0f);
                rightDoor.transform.Translate(-move, 0f, 0f);
            }
        }
    }

    private void OnTriggerEnter(Collider other)
    {
        if (other.CompareTag("Player"))
        {
            audioSource.Stop();
            audioSource.clip = doorsOpen;
            isOppening = true;
            audioSource.Play();
        }
    }

    private void OnTriggerExit(Collider other)
    {
        if (other.CompareTag("Player"))
        {
            audioSource.Stop();
            audioSource.clip = doorsClose;
            isOppening = false;
            audioSource.Play();
        }
    }
}
